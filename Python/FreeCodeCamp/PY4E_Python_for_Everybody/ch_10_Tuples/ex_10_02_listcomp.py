# Exercise 2: This program counts the distribution of the hour of the day for
# each of the messages. You can pull the hour from the “From” line by finding
# the time string and then splitting that string into parts using the colon
# character. Once you have accumulated the counts for each hour, print out
# the counts, one per line, sorted by hour as shown below.

# python timeofday.py

# Enter a file name: mbox-short.txt
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)

di = dict()
for line in fh:
    line = line.rstrip().split()
    if 'From' in line:
        timestamp = line[5]
        hour = timestamp.split(':')[0]
        di[hour] = di.get(hour, 0) + 1

times = sorted([(key, val) for key, val in di.items()])

print("\n")
for key, val in times:
    print(key, val)
