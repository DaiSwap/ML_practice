#brute force it - sort and check each neighbours , 
# O(nlogn) & O(1)
for i in range(1,n-1):
    if i==i-1:
        return True
    else:
        return False


# use hash net , compromise on space complexity but increase the time complexity
# O(n)&O(n)
hashset = set()
for n in nums:
    if n in hashset:
        print(True)
    hashnet.add(n)
print(False)

#Further DSA solved directly on leetcode - refer id - https://leetcode.com/u/DaiSwap/