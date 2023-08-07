#!/usr/bin/python3
for num in range(10):
    for n in range(10):
        if num == 8 and n == 9:
            print("89")
        elif num < n:
            print("{:d}{:d}".format(num, n), end=", ")
            