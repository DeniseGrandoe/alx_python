#!/urs/bin/python3
def fibonacci_sequence(n):
    fib = [0, 1]
    if n == 0:
        return []
    elif n == 1:
        return [0]
    else:
        while len(fib) < n:
            cel = fib[-1] + fib[-2]
            fib.append(cel)
        return fib
  


        
    