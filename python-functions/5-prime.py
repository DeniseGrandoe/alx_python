#!/urs/bin/python3
def is_prime(number):
    if number <=1:
        return False
    else:
        for i in range(2,number):
            if number % i == 0:
                return False
            return True