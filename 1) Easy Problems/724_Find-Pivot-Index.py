class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        Total = sum(nums)
        left = 0

        for index in range(0, len(nums)):   # for each index (possible pivot)
            if left == (Total-nums[index])/2:  # if strictly to left == strictly to right
                return index                # return the pivot
            else:
                left += nums[index]
        
        return -1  # did not find a valid pivot


    '''   
class Solution(object):
    def pivotIndex(self, nums):
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):  # i is index, x is value at index (x = nums[i])
            if leftsum == (S - leftsum - x):
                return i       # return index ("pivot")
            leftsum += x
        return -1
    '''
