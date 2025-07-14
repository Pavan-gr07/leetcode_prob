def containMostWater():
    heights = [1,8,6,2,5,4,8,3,7]

    left  = 0
    right = len(heights) - 1
    area = 0
    while left < right:
        length = min(heights[left],heights[right])
        breadth = (right - left)
        if ((length * breadth) > area):
            area =  length * breadth
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return area

print(containMostWater())