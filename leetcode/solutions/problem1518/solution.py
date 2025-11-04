class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drink = 0
        while numBottles > 0:
            replace = numBottles//numExchange
            drink += (replace*numExchange)
            numBottles = numBottles%numExchange+replace
            if numBottles < numExchange:
                drink += numBottles
                break
        return drink

