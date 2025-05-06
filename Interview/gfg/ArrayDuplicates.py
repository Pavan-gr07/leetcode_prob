# package Interview;

# import java.util.*;

# public class Solution {
#     public List<Integer> findDuplicates(int[] arr) {
#         List<Integer> ans = new ArrayList<>();
#         Map<Integer, Integer> dict = new HashMap<>();

#         for (int i = 0; i < arr.length; i++) {
#             dict.put(arr[i], dict.getOrDefault(arr[i], 0) + 1);
#         }

#         for (Map.Entry<Integer, Integer> entry : dict.entrySet()) {
#             if (entry.getValue() > 1) {
#                 ans.add(entry.getKey());
#             }
#         }

#         return ans;
#     }
# }



def findDuplicates(arr):
    ans = []
    dict = {}
    for i in range(len(arr)):
        if arr[i] in dict:
           dict[arr[i]] += 1
        else:
           dict[arr[i]] = 1
    for ele in dict.items():
        if ele[1] > 1:
            ans.append(ele[0])
    return ans
    
# TC - O(n+n)
# SC - O(n)
print(findDuplicates([2,3,1,2,3]))