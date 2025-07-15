/*
Leetcode 2523 Closest Prime Nummbers in Range
Given two positive integers left and right, find the two integers num1 and num2 such that:

left <= num1 < num2 <= right .
Both num1 and num2 are prime numbers.
num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].

*/


import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int[] closestPrimes(int left, int right) {
        if (left >= right || right > 1_000_000) {
            return new int[] {-1, -1};
        }

        boolean[] isPrime = sieveOfEratosthenes(right);
        ArrayList<Integer> primesInRange = new ArrayList<>();

        for (int i = left; i <= right; i++) {
            if (isPrime[i]) {
                primesInRange.add(i);
            }
        }

        if (primesInRange.size() < 2) {
            return new int[] {-1, -1};
        }

        int minDiff = Integer.MAX_VALUE;
        int num1 = -1, num2 = -1;

        for (int i = 1; i < primesInRange.size(); i++) {
            int diff = primesInRange.get(i) - primesInRange.get(i - 1);
            if (diff < minDiff) {
                minDiff = diff;
                num1 = primesInRange.get(i - 1);
                num2 = primesInRange.get(i);
                if (minDiff <= 2) {
                    break;
                }
            }
        }

        return new int[] {num1, num2};
    }

    private boolean[] sieveOfEratosthenes(int n) {
        boolean[] isPrime = new boolean[n + 1];
        Arrays.fill(isPrime, true);
        isPrime[0] = isPrime[1] = false;

        for (int i = 2; i * i <= n; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= n; j += i) {
                    isPrime[j] = false;
                }
            }
        }

        return isPrime;
    }
}
