class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        n = len(s)

        l = 0
        r = 1
        car_set = set(s[:1])

        max_len = 0
        while r < n:
            curr_car = s[r]
            if curr_car not in car_set:
                car_set.add(curr_car)
            else:
                max_len = max(max_len, r - l)
                while l < r and curr_car in car_set:
                    car_set.remove(s[l])
                    l += 1
                car_set.add(curr_car)
            
            r += 1
        max_len = max(max_len, r - l)
        return max_len