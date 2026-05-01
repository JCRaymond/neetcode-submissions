class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_car_counts = [0]*26
        t_car_counts = [0]*26

        oa = ord('a')
        for car in s:
            s_car_counts[ord(car) - oa] += 1
        for car in t:
            t_car_counts[ord(car) - oa] += 1
        
        return s_car_counts == t_car_counts