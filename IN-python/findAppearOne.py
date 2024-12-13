arr = [5,4,5,3,2,4,3]


# frequency of an array
dict = {}
count = 1
for num in arr:
    if num in dict:
        dict[num] = count +1
    else:
        dict[num] = 1

for num in dict:
    if dict[num] ==1:
        print(num)

# O(n) --> time complexity
# O(n) --> space complexity

print(5^4,5,3,2,4,3)
  




