# Exercise 2: Write a program that categorizes each mail message by which day
# of the week the commit was done. To do this look for lines that start with
# “From”, then look for the third word and keep a running count of each of
# the days of the week. At the end of the program print out the contents of
# your dictionary (order does not matter).

# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

# Sample Execution:
# python dow.py
# Enter a file name: mbox-short.txt
# {'Fri': 20, 'Thu': 6, 'Sat': 1}

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
ddd = dict()

for line in fh :
    line = line.rstrip().split()
    if not 'From' in line: continue
    day = line[2]
    ddd[day] = ddd.get(day, 0) + 1

print("\n")
print(ddd)
