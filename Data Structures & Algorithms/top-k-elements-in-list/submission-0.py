class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for num in nums:
            if num not in frequencies:
                frequencies[num] = 1
            else:
                frequencies[num] += 1
        
        frequency_buckets = [[] for _ in range(len(nums))]
        for num, freq in frequencies.items():
            frequency_buckets[freq-1].append(num)

        topK = [None]*k
        i = 0
        for freq_bucket in reversed(frequency_buckets):
            if i >= k:
                break
            for num in freq_bucket:
                topK[i] = num
                i += 1
        return topK
                
