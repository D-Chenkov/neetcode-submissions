class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Naive
        #for i in range(len(nums)):
        #    for j in range(len(nums)):
        #        if (i!=j):
        #            if nums[i] + nums[j] == target:
        #                return [i, j]

        #Hashing
        seen = {}
        for i, num in enumerate(nums):
            complement = target-num
            if (complement) in seen:
                return[seen[complement], i]
            seen[num] = i