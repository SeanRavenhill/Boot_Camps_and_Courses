# See README.md for assignment brief.

import re

fn = input("Enter file: ")
if len(fn) < 1: fn = "regex_sum_941919.txt"
fh = open(fn)

count = 0
total = 0

for line in fh:
    line = line.rstrip()
    x = re.findall('([0-9]+)', line)
    for n in x :
        n = int(n)
        total = total + n
        count += 1

print(count)
print(total)
