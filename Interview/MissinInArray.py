def missingElement(arr):
    s = set(arr)
    for i in range(1,len(arr)+2):
            if i not in s:
                return i
            

# class Solution {
#     int missingNum(int arr[]) {
#         // code here
#         Set<Integer> s = new HashSet<>();
#         for(int ele : arr)
#         {
#             s.add(ele);
#         }
        
#         for( int i=1;i<arr.length +2;i++)
#         {
#             if(!s.contains(i))
#             {
#                 return i;
#             }
#         }
#         return 0;
        
#     }
# }

print(missingElement([1]))
