class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        max_bottles = empty = 0
        while numBottles > 0:
            max_bottles += numBottles
            empty += numBottles
            numBottles = 0
            while empty >= numExchange:
                empty -= numExchange
                numExchange += 1
                numBottles += 1
        return max_bottles
