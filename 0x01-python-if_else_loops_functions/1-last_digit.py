#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(repr(number)[-1])
if last_digit > 5:
    print("Last digit of {} is {} and is greater than {}".format(number, last_digit, 5))
elif last_digit == 0:
    print("Last digit of {} is {} and is {}".format(number, last_digit), 0)
else:
    ("Last digit of {} is {} and is less than {} and not {}".format(number, last_digit), 6, 0)
