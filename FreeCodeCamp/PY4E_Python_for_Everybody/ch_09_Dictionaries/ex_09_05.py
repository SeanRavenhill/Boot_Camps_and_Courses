# Exercise 5: This program records the domain name (instead of the address)
# where the message was sent from instead of who the mail came from
# (i.e., the whole email address). At the end of the program, print out the
# contents of your dictionary.

# python schoolcount.py

# Enter a file name: mbox-short.txt

# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
# 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)

ddd = dict()
for line in fh :
    line = line.rstrip().split()
    if not 'From' in line : continue
    email = line[1]
    domain = email.split('@')[1]
    ddd[domain] = ddd.get(domain, 0) + 1

print("\n")
print(ddd)
