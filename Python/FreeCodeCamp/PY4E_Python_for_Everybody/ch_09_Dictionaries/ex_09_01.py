# Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt

# Write a program that reads the words in words.txt and stores them as keys
# in a dictionary. It doesn’t matter what the values are. Then you can use
# the in operator as a fast way to check whether a string is in the dictionary.

fname = input("Enter file: ")
if len(fname) < 1 : fname = "words.txt"
fh = open(fname)

ddd = dict()
for line in fh:
    line = line.rstrip().split()
    words = line
    for word in words:
        ddd[word] = ddd.get(word,0) + 1

print("\n")
print(ddd)
