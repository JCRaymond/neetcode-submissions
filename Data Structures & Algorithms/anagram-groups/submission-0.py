class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}
        oa = ord('a')
        for s in strs:
            car_counts = [0]*26
            for car in s:
                car_counts[ord(car) - oa] += 1
            
            key = tuple(car_counts)
            if key not in anagram_groups:
                anagram_groups[key] = [s]
            else:
                anagram_groups[key].append(s)
        
        return list(anagram_groups.values())