class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        long_pali_idx = 0
        long_pali_len = 1

        for i in range(n-1):

            left = i
            right = i
            
            while left > 0 and right < n-1:
                if s[left-1] != s[right+1]:
                    break

                left -= 1
                right += 1
            
            odd_pali_len = right - left + 1
            if odd_pali_len > long_pali_len:
                long_pali_idx = left
                long_pali_len = odd_pali_len
            

            left = i+1
            right = i

            while left > 0 and right < n-1:
                if s[left-1] != s[right+1]:
                    break

                left -= 1
                right += 1
            
            even_pali_len = right - left + 1
            if even_pali_len > long_pali_len:
                long_pali_idx = left
                long_pali_len = even_pali_len
            
        return s[long_pali_idx:long_pali_idx + long_pali_len]
