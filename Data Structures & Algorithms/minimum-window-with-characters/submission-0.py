class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        n = len(s)
        t_counts = {}

        for car in t:
            t_counts[car] = 1 + t_counts.get(car, 0)
        cars_fulfilled = 52 - len(t_counts)

        l = 0
        r = 0
        min_len = n+1
        min_substr = ""
        window_counts = {}
        while r < n:
            curr_car = s[r]
            window_counts[curr_car] = 1 + window_counts.get(curr_car, 0)
            if window_counts[curr_car] == t_counts.get(curr_car, 0):
                cars_fulfilled += 1
            r += 1
            
            if cars_fulfilled == 52:
                while cars_fulfilled == 52:
                    curr_car = s[l]
                    window_counts[curr_car] -= 1
                    if window_counts[curr_car] == t_counts.get(curr_car, 0) - 1:
                        cars_fulfilled -= 1
                    l += 1
                
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_substr = s[l-1:r]


        return min_substr
