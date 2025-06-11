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

lst = [(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627)]
for _ in range(100):
    n = random.randint(1, 1000)
    lst.append((random.randint(10**n, 10**(n+1)-1),random.randint(10**n, 10**(n+1)-1)))
    
fail = False 
count = 0
for x, y in lst:
    count+=1
    ans = multiply(x,y)
    
    if x*y != ans:
        fail = True
        break
print("Fail" if fail else "Success!!", count)
