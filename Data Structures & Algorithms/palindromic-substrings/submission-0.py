class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        pali_count = 1 # Last character is a palindrome

        for i in range(n-1):

            left = i
            right = i
            pali_count += 1
            
            while left > 0 and right < n-1:
                if s[left-1] != s[right+1]:
                    break
                
                pali_count += 1
                left -= 1
                right += 1
            

            left = i+1
            right = i

            while left > 0 and right < n-1:
                if s[left-1] != s[right+1]:
                    break

                pali_count += 1

                left -= 1
                right += 1

        return pali_count

        