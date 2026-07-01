class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Two Ways Hash and then o(1)
        if len(nums) != len(set(nums)):
            return True
        return False
        
        # Hardcode count every number individually o(n)
        #
        #for num in nums:
        #    if nums.count(num) > 1:
        #        print(nums.count(num))
        #        print(num)
        #        return True
        #return False

        #Optimized for SPACE 
        #nums.sort()
        #for i in range(len(nums) -1):
        #    if nums[i] == nums[i+1]:
        #        return True
        #return False