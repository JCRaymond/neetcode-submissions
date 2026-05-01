class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen_nums = {
            num: False
            for num in nums
        }

        max_chain_len = 0
        for num in seen_nums:
            if seen_nums[num]:
                continue
            
            chain_len = 1
            # Forward chain
            curr_num = num
            while curr_num + 1 in seen_nums:
                chain_len += 1
                seen_nums[curr_num + 1] = True
                curr_num += 1
            
            # Backward chain
            curr_num = num
            while curr_num - 1 in seen_nums:
                chain_len += 1
                seen_nums[curr_num - 1] = True
                curr_num -= 1
            
            max_chain_len = max(max_chain_len, chain_len)
        
        return max_chain_len