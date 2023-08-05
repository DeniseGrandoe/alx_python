#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if number > 0 :
    print ('{} number is positvie' .format(number))
elif number == 0:
    print('{} number is zero' .format(number))
else:
    print ('{} number is negatve' .format(number))
