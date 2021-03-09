# Exercise 2: Write a program to look for lines of the form:

# New Revision: 39772

# Extract the number from each of the lines using a regular expression
# and the findall() method. Compute the average of the numbers and
# print out the average as an integer.

# Enter file:mbox.txt
# 38549
# Enter file:mbox-short.txt
# 39756

import re

fn = input("Enter file: ")
if len(fn) < 1: fn = "mbox.txt"
fh = open(fn)

count = 0
total = 0

for line in fh:
    line = line.rstrip()
    x = re.findall('^New Revision: ([0-9]+)', line)
    for n in x :
        n = int(n)
        total = total + n
        count = count + 1

print(int(total/count))
