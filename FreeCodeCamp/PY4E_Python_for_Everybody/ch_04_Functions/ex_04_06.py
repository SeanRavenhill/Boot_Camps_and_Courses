# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and
# create a function called computepay which takes two parameters (hours and rate).

def computepay(h,r):
    if h > 40 :
        rgh = h * r
        otp = (h - 40) * (r * 0.5)
        p = rgh + otp
    else:
        p = h * r
    return p

hrs = input("Enter your hours: ")
rts = input("Enter your rate: ")

try:
    h = float(hrs)
    r = float(rts)
except:
    print("Error, please enter numeric input.")
    quit()

pay = computepay(h,r)

print('\n' + 'Pay:', round(pay, 2))
