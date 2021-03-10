# Exercise 1: Write a function called chop that takes a list and modifies it,
# removing the first and last elements, and returns None. Then write a function
# called middle that takes a list and returns a new list that contains all
# but the first and last elements.

def chop(lst):
    del lst[0]
    del lst[-1]

def middle(lst):
    return lst[1:-1]

mylist = [1,2,3,4,5,6,7,8,9,10]
mylist2 = [1,2,3,4,5,6,7,8,9,10]

chop = chop(mylist)
print(chop)

middle = middle(mylist2)
print(middle)
