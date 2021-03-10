# Exercise 3: Write a program that reads a file and prints the letters in
# decreasing order of frequency. Your program should convert all the input
# to lower case and only count the letters a-z. Your program should not count
# spaces, digits, punctuation, or anything other than the letters a-z. Find
# text samples from several different languages and see how letter frequency
# varies between languages. Compare your results with the tables at
# https://wikipedia.org/wiki/Letter_frequencies.

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "eng.txt"
fh = open(fname)

alphabet = 'abcdefghijklmnopqrstuvxwyz'

di = dict()
for line in fh :
    line = line.strip().lower().split()
    for words in line :
        words = words
        for chars in words :
            chars = chars
            if chars in alphabet :
                di[chars] = di.get(chars, 0) + 1
            else:
                continue

ordered = sorted( [(val, key) for key, val in di.items()], reverse=True)

print("\n")
for val, key in ordered:
    print(key, val)
