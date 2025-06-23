# Solution for problem 2081
class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def rev(num):
            r_num = 0
            while num > 0:
                d = num%10
                r_num = r_num * 10 + d
                num//=10
            return r_num
        def base10_to_k_is_pal(num, k):
            digits = []
            while num > 0:
                digits.append(num % k)
                num //= k
            return digits == digits[::-1]
            
        ans = 0
        for num in range(1,10):
            if base10_to_k_is_pal(num, k):
                n-=1
                ans+=num
                if n == 0:
                    return ans

            
        length = 2
        while True:
            half_len = length//2
            start, end = 10**(half_len-1), 10**(half_len)
            for first in range(start, end):
                if length % 2 == 1:
                    for mid in range(10):
                        num = first*10**(half_len+1)+mid*10**half_len+rev(first)
                        if base10_to_k_is_pal(num, k):
                            n-=1
                            ans += num
                        if n == 0:
                            return ans
                else:
                    num = first*10**(half_len)+rev(first)
                    if base10_to_k_is_pal(num, k):
                        n-=1
                        ans += num
                    if n == 0:
                        return ans
            length+=1
