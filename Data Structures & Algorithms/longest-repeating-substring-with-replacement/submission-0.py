class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        r = 0

        counts = {}
        max_freq = 0
        max_len = 0
        while r < n:
            curr_car = s[r]
            if curr_car not in counts:
                counts[curr_car] = 1
            else:
                counts[curr_car] += 1
            max_freq = max(max_freq, counts[curr_car])

            while (r + 1 - l) - max_freq > k:
                counts[s[l]] -= 1
                l += 1
            
            max_len = max(max_len, r+1-l)
            r += 1
            
        return max_len