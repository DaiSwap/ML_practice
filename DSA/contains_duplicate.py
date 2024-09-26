#brute force it - sort and check each neighbours , 
# O(nlogn) & O(1)
nums = [1,2,3,4,6,7,5,6]
nums.sort()
for i in range(1,len(nums)):
    if nums[i]==nums[i-1]:
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