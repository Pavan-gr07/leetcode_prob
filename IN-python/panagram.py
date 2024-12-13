# Input 1: “The quick bown fox jumps over the lazy dog”
# Output 1: true
# Explanation 1: Contains all the characters from ‘a’ to ‘z’


# 97-122

# def panagram(str):
#     thisSet = set()
#     for ele in str:
#         if  ele.isalnum() and ele.islower() and ord(ele)>=97 and ord(ele)<=122:
#             thisSet.add(ele)
#     return len(thisSet)==26
def panagram(str):
    arr = [0]*26
    cnt= 0
    print(arr)
    for ele in str:
        if ele.islower():
            idx = ord(ele) - ord('a')

            if arr[idx] ==0:
                arr[idx] +=1
                cnt += 1
        
    return cnt==26



print(panagram('The quick brown fo jumps over the lazy dog'))