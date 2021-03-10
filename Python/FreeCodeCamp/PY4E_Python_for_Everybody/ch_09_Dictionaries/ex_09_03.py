# Exercise 3: Write a program to read through a mail log, build a histogram
# using a dictionary to count how many messages have come from each email
# address, and print the dictionary.

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
ddd = dict()

for line in fh :
    line = line.rstrip().split()
    if not 'From' in line: continue
    email = line[1]
    ddd[email] = ddd.get(email, 0) + 1

print("\n")
print(ddd)
