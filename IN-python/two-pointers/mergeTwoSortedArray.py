list1 = [1,2,3,4]
list2 = [1,2,3,4]


def mergeTwoSortedList(list1, list2):
    ans = list1 + list2  # O(n + m)
    ans.sort()  # O((n + m) log(n + m))
    return ans

# TC - O((n + m) log(n + m))

def mergeTwoSortedArray(list1,list2):
    i,j = 0,0
    ans = []
    while i<len(list1) and j<len(list2):
        if list1[i] < list2[j]:
            ans.append(list1[i])
            i+=1
        else:
            ans.append(list2[j])
            j+=1

    ans.extend(list1[i:])
    ans.extend(list2[j:])
    return ans

# TC - O(n+m)
# SC - O(n)
print(mergeTwoSortedArray(list1,list2))