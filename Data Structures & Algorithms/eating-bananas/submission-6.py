from math import ceil

class Solution:

    def calc_hours(piles, speed):
        hours = 0
        for pile in piles:
            hours += ceil(pile/speed)
        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        speed_lo = 0
        speed_hi = max(piles)

        while speed_hi - speed_lo > 1:
            print(speed_lo, speed_hi, flush=True)
            speed_m = (speed_hi + speed_lo)//2
            hours_m = 0
            for pile in piles:
                hours_m += ceil(pile/speed_m)
            print(speed_m, hours_m)
            if h < hours_m:
                speed_lo = speed_m
            else:
                speed_hi = speed_m
        
        print(speed_lo, speed_hi)
        return speed_hi

