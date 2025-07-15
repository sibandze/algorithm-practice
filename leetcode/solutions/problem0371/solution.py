# Leetcode 371 Sum of Two Integers
# Given two integers a and b, return the sum of the two integers without using the operators + and -.
class Solution:
    def subtract(self, a: int, b: int) -> int:
        if a == b:
            return 0
        neg = False
        if a < b:
            neg = True
            a, b = b, a
        while b != 0:
            borrow = (~a) & b
            a = a ^ b
            b = borrow << 1
        return a if not neg else -a
    def getSum(self, a: int, b: int) -> int:
        if a * b > 0:
            neg = False
            if a < 0:
                neg = True
                a = abs(a)
                b = abs(b)
            while b != 0:
                carry = a & b
                a = a ^ b
                b = carry << 1
            return a if not neg else -a
        elif a*b == 0:
            return a if b == 0 else b
        else:
            if a > 0:
                return self.subtract(a, abs(b))
            return self.subtract(b, abs(a))
