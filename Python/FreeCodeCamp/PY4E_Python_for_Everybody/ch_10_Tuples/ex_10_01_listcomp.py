# Exercise 1: Revise a previous program as follows: Read and parse the “From”
# lines and pull out the addresses from the line. Count the number of messages
# from each person using a dictionary.

# After all the data has been read, print the person with the most commits
# by creating a list of (count, email) tuples from the dictionary.
# Then sort the list in reverse order and print out the person who has
# the most commits.

# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5

# Enter a file name: mbox.txt
# zqian@umich.edu 195

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)

di = dict()
for line in fh:
    line = line.rstrip().split()
    if 'From' in line:
        word = line[1]
        di[word] = di.get(word, 0) + 1

li = sorted([(val, key) for key, val in di.items()],reverse=True)

print("\n")
for val, key in li[:1]:
    print(key, val)
