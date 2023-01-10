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

            '''         # Double Pass Hash Map Solution
    class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]] 
    '''

    '''                 # Single Pass Hash Map Solution
    class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
    '''
