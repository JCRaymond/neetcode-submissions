class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_counts = [float('inf')]*(amount+1)

        min_counts[0] = 0

        for amt in range(1, amount+1):
            curr_count = min_counts[amt]
            for coin in coins:
                if amt - coin < 0:
                    continue
                curr_count = min(curr_count, min_counts[amt - coin])
            min_counts[amt] = curr_count + 1
        
        if min_counts[-1] == float('inf'):
            min_counts[-1] = -1

        return min_counts[-1]
            
