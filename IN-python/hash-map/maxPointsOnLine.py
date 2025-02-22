# 149. Max Points on a Line
# Hard
# Topics
# Companies
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

 

# Example 1:


# Input: points = [[1,1],[2,2],[3,3]]
# Output: 3
# Example 2:


# Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4


from collections import defaultdict
def maxPoints( points) :
        if len(points) <= 2:
            return len(points)
        
        def find_slope(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            if x1-x2 == 0:
                return float("inf")
            return (y1-y2)/(x1-x2)
        
        ans = 1
        for i, p1 in enumerate(points):
            slopes = defaultdict(int)
            for j, p2 in enumerate(points[i+1:]):
                slope = find_slope(p1, p2)
                slopes[slope] += 1
                ans = max(slopes[slope], ans)
        return ans+1 

from math import gcd

def maxPoints1(points):
    if len(points) <= 2:
        return len(points)

    max_count = 1  # At least one point is always on a line
    
    for i, (x1, y1) in enumerate(points):
        slopes = defaultdict(int)
        duplicates = 1  # Count duplicate points at the same location

        for j in range(i+1, len(points)):
            x2, y2 = points[j]
            dx, dy = x2 - x1, y2 - y1
            
            if dx == 0 and dy == 0:
                duplicates += 1  # Same point
                continue
            
            g = gcd(dx, dy)
            slope = (dx // g, dy // g)  # Store slope as reduced fraction
            
            slopes[slope] += 1
            max_count = max(max_count, slopes[slope] + duplicates)  # Include duplicates

    return max_count+1

print(maxPoints1([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))