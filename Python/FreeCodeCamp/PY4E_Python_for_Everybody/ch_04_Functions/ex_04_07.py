# Exercise 7: Rewrite the grade program from the previous chapter using a
# function called computegrade that takes a score as its parameter and returns
# a grade as a string.

def computegrade(grade):
    if grade > 1.0 :
        print("Bad Score.")
    elif grade >= 0.9 :
        print("You scored a A")
    elif grade >= 0.8 :
        print("You scored a B")
    elif grade >= 0.7 :
        print("You scored a C")
    elif grade >= 0.6 :
        print("You scored a D")
    elif grade < 0.6 :
        print("You scored a F")

score = input("Enter Score: ")

try:
    grade = float(score)
except:
    print("Please enter a numberic value.")
    quit()

computegrade(grade)
