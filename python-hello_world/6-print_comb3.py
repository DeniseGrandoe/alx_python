#!/usr/bin/python3
for num in range(0, 10):
    for n in range(0, 10):
        if num < n:
            print("{:d}{:d}".format(num, n), end="")
            if num < 8:
                print(", ", end="")
            