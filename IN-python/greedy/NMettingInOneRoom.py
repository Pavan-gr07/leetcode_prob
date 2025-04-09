# # N meetings in one room
# Greedy
# easy
# Score: 20
# Microsoft
# MakeMyTrip
# Flipkart
# There is one meeting room in a firm. There are N meetings in the form of (start[i], end[i]) where start[i] is start time of meeting i and end[i] is finish time of meeting i. What is the maximum number of meetings that can be accommodated in the meeting room when only one meeting can be held in the meeting room at a particular time?

# Note: Start time of one chosen meeting can’t be equal to the end time of the other chosen meeting.

# Input Format
# The first line contains an integer n the length of the original array a and b. The second line contains n integers a1, a2, … the array elements themselves, denoting the start time of the meeting. The third line contains n integers b1, b2, … the array elements themselves, denoting the end time of the meeting.

# Output Format
# Print the number of meetings that can be accommodated in the meeting room.

# Example 1:
# Input:
#     6
#     1 3 0 5 8 5
#     2 4 6 7 9 9
# Output:
#     4
# Explanation:
#     A maximum of four meetings can be held with
#     given start and end timings.
#     The meetings are - (1, 2),(3, 4), (5,7), and (8,9)
# Example 2:
# Input:
#     3
#     10 12 20
#     20 25 30
# Output:
#     1
# Explanation:
#     Only one meeting can be held
#     with given start and end timings.

# Constraints:
# 1 ≤ N ≤ 100000
# 0 ≤ start[i] < end[i] ≤ 100000
# Expected Time Complexity : O(N*LogN)
# Expected Auxilliary Space : O(N)

def NMettingOneRoom(a,b):
    metting = list(zip(a,b))

    metting.sort(key=lambda x:x[1])

    count = 1
    freeTime = metting[0][1]
    for i in range(1,len(metting)):
        if metting[i][0] > freeTime:
            count +=1
            freeTime = metting[i][1]
    return count

start_times = [1, 3, 0, 5, 8, 5]
end_times = [2, 4, 6, 7, 9, 9]

print(NMettingOneRoom(start_times, end_times))  # Output: 4


