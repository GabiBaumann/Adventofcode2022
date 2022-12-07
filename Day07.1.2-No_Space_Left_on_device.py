#!/usr/bin/env python
# SPDX-License-Identifier: GPL-3.0-only

"""
You can hear birds chirping and raindrops hitting leaves as the expedition proceeds. Occasionally, you can even hear much louder sounds in the distance; how big do the animals get out here, anyway?

The device the Elves gave you has problems with more than just its communication system. You try to run a system update:

$ system-update --please --pretty-please-with-sugar-on-top
Error: No space left on device

Perhaps you can delete some files to make space for the update?

You browse around the filesystem to assess the situation and save the resulting terminal output (your puzzle input). For example:

$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k

The filesystem consists of a tree of files (plain data) and directories (which can contain other directories or files). The outermost directory is called /. You can navigate around the filesystem, moving into or out of directories and listing the contents of the directory you're currently in.

Within the terminal output, lines that begin with $ are commands you executed, very much like some modern computers:

    cd means change directory. This changes which directory is the current directory, but the specific result depends on the argument:
        cd x moves in one level: it looks in the current directory for the directory named x and makes it the current directory.
        cd .. moves out one level: it finds the directory that contains the current directory, then makes that directory the current directory.
        cd / switches the current directory to the outermost directory, /.
    ls means list. It prints out all of the files and directories immediately contained by the current directory:
        123 abc means that the current directory contains a file named abc with size 123.
        dir xyz means that the current directory contains a directory named xyz.

Given the commands and output in the example above, you can determine that the filesystem looks visually like this:

- / (dir)
  - a (dir)
    - e (dir)
      - i (file, size=584)
    - f (file, size=29116)
    - g (file, size=2557)
    - h.lst (file, size=62596)
  - b.txt (file, size=14848514)
  - c.dat (file, size=8504156)
  - d (dir)
    - j (file, size=4060174)
    - d.log (file, size=8033020)
    - d.ext (file, size=5626152)
    - k (file, size=7214296)

Here, there are four directories: / (the outermost directory), a and d (which are in /), and e (which is in a). These directories also contain files of various sizes.

Since the disk is full, your first step should probably be to find directories that are good candidates for deletion. To do this, you need to determine the total size of each directory. The total size of a directory is the sum of the sizes of the files it contains, directly or indirectly. (Directories themselves do not count as having any intrinsic size.)

The total sizes of the directories above can be found as follows:

    The total size of directory e is 584 because it contains a single file i of size 584 and no other directories.
    The directory a has total size 94853 because it contains files f (size 29116), g (size 2557), and h.lst (size 62596), plus file i indirectly (a contains e which contains i).
    Directory d has total size 24933642.
    As the outermost directory, / contains every file. Its total size is 48381165, the sum of the size of every file.

To begin, find all of the directories with a total size of at most 100000, then calculate the sum of their total sizes. In the example above, these directories are a and e; the sum of their total sizes is 95437 (94853 + 584). (As in this example, this process can count files more than once!)

Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?
"""

"""
Hopeful strat:
Build up data structure of dicts, containing name and either size or a dict for directories.
{ 'a': { 'e': { 'i': 584 }, 'f': 29116, 'g': 2557, 'h.lst': 62596}, 'b.txt': 14848514, 'c.dat': 8504156, { 'd': { 'j': 4060174, 'd.log': 8033020, 'd.ext': 5626152, 'k': 7214296}}}
Then compute: if type(element) is int, add size to total of dir, if type is dict, recurse same function, pass total size back and add total to a dict. As dirnames are not uniq, use full path:
{ '/a/e': 584, '/a': 94853, '/d': 24933642, '/': 48381165} (actually, / may safely be left out, will be too big... actually drop all above max?)
"""

"""
Luckily, it's not that wild once you code :)
Rather, do a dict of dirs with sums in it, adding sizes to all subdirs.
"""

"""
--- Part Two ---

Now, you're ready to choose a directory to delete.

The total disk space available to the filesystem is 70000000. To run the update, you need unused space of at least 30000000. You need to find a directory you can delete that will free up enough space to run the update.

In the example above, the total size of the outermost directory (and thus the total amount of used space) is 48381165; this means that the size of the unused space must currently be 21618835, which isn't quite the 30000000 required by the update. Therefore, the update still requires a directory with total size of at least 8381165 to be deleted before it can run.

To achieve this, you have the following options:

    Delete directory e, which would increase unused space by 584.
    Delete directory a, which would increase unused space by 94853.
    Delete directory d, which would increase unused space by 24933642.
    Delete directory /, which would increase unused space by 48381165.

Directories e and a are both too small; deleting them would not free up enough space. However, directories d and / are both big enough! Between these, choose the smallest: d, increasing unused space by 24933642.

Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?
"""

fs_size = 70000000
required = 30000000
sizeof_dir_to_delete = fs_size

cutoff = 100000
fs = { 'R': 0 }
line = " "
me_first = True
out = 0

with open('Day07-Input', 'r') as file:
    while True:
        if not me_first:
            line = file.readline().rstrip()
        me_first = False
        if not line:
            break
        marker = line[0]
        if marker == "$":
            if line[2:4] == "cd":
                param = line[5:]
                if param == "/":
                    wd = []
                elif param == "..":
                    wd.pop()
                else:
                    wd.append(param)
                print("cd", param, wd)
            elif line[2:4] == "ls":
                index = "R"
                for i in wd:
                    index += "/" + i
                while True:
                    line = file.readline().rstrip()
                    if not line:
                        # EOF. Need a bool?
                        break
                    elif line[0] == "$":
                        ## For a start, do a bool :)
                        me_first = True
                        break
                    elif line[0] == "d":
                        dirname = index + "/" + line[4:]
                        fs[dirname] = 0 #presuming we just add filesizes...
                    else:
                        filesize = int(line.split()[0])
                        h = "R"
                        fs[h] += filesize
                        for i in wd:
                            h += "/" + i
                            fs[h] += filesize

need_to_delete = required - (fs_size - fs["R"])
print(need_to_delete)

for i in fs:
    if fs[i] <= cutoff:
        out += fs[i]
    if fs[i] >= need_to_delete:
        sizeof_dir_to_delete = min(sizeof_dir_to_delete, fs[i])

print("Answer for part one:", out)
print("Answer for part two:", sizeof_dir_to_delete)

