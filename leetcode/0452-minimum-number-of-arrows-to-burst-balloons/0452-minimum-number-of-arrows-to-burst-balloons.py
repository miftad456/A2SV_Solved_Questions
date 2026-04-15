class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1

        points.sort(key=lambda x: x[0])
        arrows = 1

        minPrevend = points[0][1]

        for start, end in points[1:]:
            if start > minPrevend:
                arrows += 1
                minPrevend = end
            minPrevend = min(minPrevend, end)
        
        return arrows