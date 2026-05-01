class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        l = 0
        r = n-1

        water = 0
        water_height = 0
        while l < r:

            water_height = max(water_height, min(height[l], height[r]))


            if height[l] < height[r]:
                l += 1
                water += max(water_height - height[l], 0)
            else:
                r -= 1
                water += max(water_height - height[r], 0)
        
        return water