"""
Turn the following unix pipeline into Python code using generators
$ for i in ../*/*py; do grep ^import $i|sed 's/import //g' ; done | sort | uniq -c | sort -nr
   4 unittest
   4 sys
   3 re
   3 csv
   2 tweepy
   2 random
   2 os
   2 json
   2 itertools
   1 time
   1 datetime
"""
import os
import re
from operator import itemgetter

def gen_files(pat, ext):
    for root, dirs, files in os.walk(pat[0:2]):
        for file in files:
            if file.endswith(ext):
                yield os.path.join(root, file)


def gen_lines(files):
    for file in files:
        with open(file, 'r') as f:
            for line in f.readlines():
                yield line

def gen_grep(lines, pattern):
    for line in lines:
        if (re.search(pattern, line)):
            yield line

def gen_count(lines):
    new_list = list(lines)
    new_list = {line.split()[1] : new_list.count(line) for line in new_list}
    sorted_dict = sorted(new_list, key = new_list.__getitem__, reverse=True)
    for item in sorted_dict:
        yield '{} {}'.format(new_list[item], item)



if __name__ == "__main__":
    # call the generators, passing one to the other
    pat = '../*/*.py'
    ext = '.py'
    regex_pat = '^import '
    files = gen_files(pat, ext)
    lines = gen_lines(files)
    keyline= gen_grep(lines, regex_pat)
    lines = gen_count(keyline)
    for line in (list(lines)):
        print (line)
    # etc