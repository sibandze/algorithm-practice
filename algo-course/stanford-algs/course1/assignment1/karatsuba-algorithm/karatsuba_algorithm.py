import random
def multiply(x,y):
    x, y = min(x,y),max(x,y)
    n = len(str(x))
    if n == 1:
        return x * y
    m = 10**(n//2)
    x1, x0 = x//m, x%m
    y1, y0 = y//m, y%m
    
    A = multiply(x1, y1)
    C = multiply(x0, y0)
    B = multiply(x1+x0, y1+y0) - A - C
    
    return A*(m**2) + B * m + C
