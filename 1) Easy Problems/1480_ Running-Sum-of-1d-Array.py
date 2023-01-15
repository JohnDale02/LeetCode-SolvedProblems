class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums

'''
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = []
        i = 0
        currSum = 0
        for number in nums:
            currSum += number
            runningSum.append(currSum)
            i += 1
        return runningSum
'''
