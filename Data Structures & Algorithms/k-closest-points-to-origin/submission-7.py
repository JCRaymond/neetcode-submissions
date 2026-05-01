class Solution:
    def quickSelectK(self, items, k, key = lambda x:x):
        if k == 1:
            return [min(items, key=key),]
        item_keys = [key(item) for item in items]
        s = 0
        e = len(items)-1
        while s < e:
            print(items, s, e)
            root_key = item_keys[e]
            
            l = s
            r = e
            while l < r:
                while l < r and item_keys[l] < root_key:
                    l += 1
                while l < r and item_keys[r] >= root_key:
                    r -= 1
                items[l], items[r] = items[r], items[l]
                item_keys[l], item_keys[r] = item_keys[r], item_keys[l]

            root = l
            items[e], items[root] = items[root], items[e]
            item_keys[e], item_keys[root] = item_keys[root], item_keys[e]

            if root == k-1 or root == k:
                return items[:k]
            elif k < root:
                e = root - 1
            else:
                s = root + 1
        return items[:s+1]
        
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return self.quickSelectK(list(points), k, lambda p: p[0]*p[0] + p[1]*p[1])