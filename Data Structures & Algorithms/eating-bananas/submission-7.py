from math import ceil

class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        speed_lo = 0
        speed_hi = max(piles)

        while speed_hi - speed_lo > 1:
            speed_m = (speed_hi + speed_lo)//2
            hours_m = 0
            for pile in piles:
                hours_m += ceil(pile/speed_m)
            if h < hours_m:
                speed_lo = speed_m
            else:
                speed_hi = speed_m
        
        return speed_hi

