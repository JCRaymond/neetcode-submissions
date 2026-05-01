from collections import Counter

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        num_counts = Counter(nums)
        digs = list(num_counts)
        counts = [num_counts[dig] for dig in digs]
        counter = [0]*len(digs)

        result = []
        while True:
            curr = []
            for i, amnt in enumerate(counter):
                for _ in range(amnt):
                    curr.append(digs[i])
            result.append(curr)

            i = 0
            counter[i] += 1
            while i < len(counter) and counter[i] > counts[i]:
                counter[i] = 0
                i += 1
                if i < len(counter):
                    counter[i] += 1
            
            if i == len(counter):
                break

        return result
        