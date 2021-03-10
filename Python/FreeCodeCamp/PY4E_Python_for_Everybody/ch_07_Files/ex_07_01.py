# Exercise 1:
# Write a program to read through a file and print the contents
# of the file (line by line) all in upper case.

# You can download the file from www.py4e.com/code3/mbox-short.txt

fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("File could not be opened:", fname)
    quit()

for line in fhand:
    line = str.upper(line.rstrip())
    print(line)
