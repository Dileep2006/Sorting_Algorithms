# The Dutch National Flag (DNF) algorithm is a 3-way partitioning algorithm used to sort an array containing three distinct values.
# it is only used for sorting purpose, when an array are divided into 3 segements this algorithms helps to sort in place
# This algorithm is used when we want in place sorting or sc = O(1) or No extra space complexity
# time complexity = O(n) and space complexity = O(1)

nums = [0,1,2,1,2,0]
def Sorting(nums):
    left = mid = 0
    high = len(nums)-1
    while mid <= high:
        if nums[mid] == 0:
            nums[left], nums[mid] = nums[mid], nums[left]
            left += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
Sorting(nums)
print(nums)