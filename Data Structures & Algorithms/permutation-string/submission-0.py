class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        win_len = len(s1)
        n = len(s2)

        oa = ord('a')
        need_counts = [0]*26
        for car in s1:
            need_counts[ord(car)-oa] += 1

        window_error = len(s1)
        window_counts = [0]*26
        for i in range(win_len):
            car_idx = ord(s2[i]) - oa
            car_needed = need_counts[car_idx]
            car_old = window_counts[car_idx]
            window_counts[car_idx] += 1
            car_new = car_old + 1
            window_error += abs(car_new - car_needed) - abs(car_old - car_needed)
        if window_error == 0:
            return True

        l = 0
        while l + win_len < n:
            car_idx = ord(s2[l]) - oa
            car_needed = need_counts[car_idx]
            car_old = window_counts[car_idx]
            window_counts[car_idx] -= 1
            car_new = car_old - 1
            window_error += abs(car_new - car_needed) - abs(car_old - car_needed)

            car_idx = ord(s2[l + win_len]) - oa
            car_needed = need_counts[car_idx]
            car_old = window_counts[car_idx]
            window_counts[car_idx] += 1
            car_new = car_old + 1
            window_error += abs(car_new - car_needed) - abs(car_old - car_needed)

            if window_error == 0:
                return True

            l += 1
        
        return False


