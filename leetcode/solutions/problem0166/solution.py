class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = 1
        if numerator / denominator < 0:
            sign = -1
        
        numerator, denominator = abs(numerator), abs(denominator)
        whole = numerator//denominator

        rem = numerator%denominator
        if rem == 0:
            return str(sign*whole)
        sign = '' if sign == 1 else '-'
        seen_rem = {}
        decimals = []
        pos = 0
        while rem != 0:
            if rem not in seen_rem:
                seen_rem[rem] = pos
                rem *= 10
                decimals.append(str(rem//denominator))
                rem %= denominator
                pos+=1
            else:
                break
        if rem == 0:
            return f"{sign}{whole}.{''.join(decimals)}"
        else:
            return f"{sign}{whole}.{''.join(decimals[:seen_rem[rem]])}({''.join(decimals[seen_rem[rem]:])})"
