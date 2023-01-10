class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        slide = 0
        endindex = len(nums)-1

        while slide != endindex:
            startlook = slide + 1 
            find = target - nums[slide]
            for index in range(startlook, endindex + 1):
                if nums[index] == find:
                    return [slide, index]
                else:
                    continue
            slide += 1
