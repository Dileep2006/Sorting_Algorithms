# Merge Sort
# Time complexity --> (log(n)*n)
# space complexity --> O(n)

class Solution:
    def sort(self, nums: list[int]) -> list[int]:

        def mergeSort(left, right):
            if left >= right:  # start < end where start and end access single element in last element
                return 
            
            mid = left + (right - left) // 2
            mergeSort(left, mid)
            mergeSort(mid+1, right)

            merge(left, mid, right)
        
        def merge(left, mid, right):
            temp = []
            i = left 
            j = mid + 1

            while i <= mid and j <= right:
                if nums[i] < nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            
            while i <= mid:
                temp.append(nums[i])
                i += 1
            
            while j <= right:
                temp.append(nums[j])
                j += 1

            for k in range(len(temp)):
                nums[left+k] = temp[k]


        mergeSort(0, len(nums)-1)
        return nums
    
sol = Solution()
print(sol.sort([3,23,41,45,27,3,7,83]))