
class Solution:
    def findRadius(self, houses, heaters):
        heaters.sort()
        radius = 0
        
        for house in houses:
            idx = bisect_left(heaters, house)
            
            left = float('inf')
            right = float('inf')
            
            if idx > 0:
                left = house - heaters[idx - 1]
            if idx < len(heaters):
                right = heaters[idx] - house
            
            radius = max(radius, min(left, right))
        
        return radius