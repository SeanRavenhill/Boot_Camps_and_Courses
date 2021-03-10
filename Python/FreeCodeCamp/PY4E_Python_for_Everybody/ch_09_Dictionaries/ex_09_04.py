# Exercise 4: Add code to the above program to figure out who has the most
# messages in the file. After all the data has been read and the dictionary
# has been created, look through the dictionary using a maximum loop
# (see Chapter 5: Maximum and minimum loops) to find who has the most messages
# and print how many messages the person has.

#Enter a file name: mbox-short.txt
#cwen@iupui.edu 5

#Enter a file name: mbox.txt
#zqian@umich.edu 195

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)

# This parses the file for received mails addresses and stores them as a histogram/dictionary.
ddd = dict()
for line in fh :
    line = line.rstrip().split()
    if not 'From' in line : continue
    email = line[1]
    ddd[email] = ddd.get(email, 0) + 1

# This creates a maximum loop to see which email address occurs the most times.
sent = None
sender = None
for key, count in ddd.items() :
    if sent is None or count > sent :
        sender = key
        sent = count

print("\n")
print(sender, sent)
