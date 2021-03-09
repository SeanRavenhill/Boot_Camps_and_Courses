# Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the
# score is out of range, print an error message. If the score is between 0.0
# and 1.0, print a grade using the following table:

'''
Score   Grade
>= 0.9     A
>= 0.8     B
>= 0.7     C
>= 0.6     D
 < 0.6     F
'''

score = input('Enter Score: ')

try:
    score_input = float(score)

except:
    print('Bad Score. Please enter numeric value.')
    quit()

if score_input > 1.0 :
    print('Bad Score. Score can not exceed 1.0.')
    quit()

grade = ''

if score_input >= 0.9 :
    grade = 'A'
elif score_input >= 0.8 :
    grade = 'B'
elif score_input >= 0.7 :
    grade = 'C'
elif score_input >= 0.6 :
    grade = 'D'
else:
    grade = 'F'

print('You scored a ' + grade)
