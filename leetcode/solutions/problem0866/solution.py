# Solution for problem 0866

class Solution:
    def primePalindrome(self, n: int) -> int:
        small_primes = {2, 3, 5, 7, 11, 13}
        def is_prime(n):
            if n < 2:
                return False
            if n in small_primes:
                return True
            for prime in small_primes:
                if n%prime == 0:
                    return False
                
            for i in range(5, int(math.sqrt(n)) + 1, 6):
                if n % i == 0 or n % (i + 2) == 0:
                    return False
            return True

        length = len(str(n))
        if length == 1:
            for num in range(n, 10):
                if is_prime(num):
                    return num
        length = max(2, length)
        while True:
            half_len = length//2
            start = int(10**(half_len-1))
            end = int(10 ** half_len)
            for first_half in range(start, end):
                r = str(first_half)[::-1]
                if length%2 == 1:
                    for mid in range(10):
                        num = int(f'{first_half}{mid}{r}')
                        if num>=n and is_prime(num):
                            return num
                else:
                    num = int(f'{first_half}{r}')
                    if num>=n and is_prime(num):
                        return num

            length+=1
