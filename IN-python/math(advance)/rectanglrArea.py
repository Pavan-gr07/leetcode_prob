# 223. Rectangle Area
# Solved
# Medium
# Topics
# Companies
# Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.

# The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).

# The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).

 

# Example 1:

# Rectangle Area
# Input: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
# Output: 45
# Example 2:

# Input: ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
# Output: 16
 

# Constraints:

# -104 <= ax1 <= ax2 <= 104
# -104 <= ay1 <= ay2 <= 104
# -104 <= bx1 <= bx2 <= 104
# -104 <= by1 <= by2 <= 104
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 240.3K
# Submissions
# 510.9K
# Acceptance Rate
# 47.0%

def computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        first_rect = (ax2-ax1) * (ay2-ay1)
        second_rect = (bx2-bx1) * (by2 - by1)

        overlap_x = max(0,min(ax2,bx2) - max(ax1,bx1))
        overlap_y = max(0,min(ay2,by2) - max(ay1,by1))
        over_all = overlap_x * overlap_y

        return first_rect + second_rect - over_all