fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print("File could not be opened:", fname)
    quit()

count = 0

for line in fh:
    line = line.rstrip().split()

    if not 'From' in line :
        continue
    count = count + 1
    word = line[1]
    print(word)

print("\nThere were", count, "lines in the file with From as the first word")
