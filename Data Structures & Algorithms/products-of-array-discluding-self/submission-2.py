class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #ah, [1,2,3] [2,3] [1,3] [1,2]
        #Naive SNEAKY, need to cover negative numbers and 0.
        #total = {}
        #for i in range(len(nums)):
        #    print(nums[i])
        #    print(math.prod(nums))
        #    total[i] = math.prod(nums)//nums[i]
        #return list(total.values())

        #ignoring 0 is gouche so let's just make this better with
        #tot = {}
        #for i in range(len(nums)):
        #    tot[i] = math.prod([num for idx, num in enumerate(nums) if idx != i])
        #return list(tot.values())

        #O(n) version
        n = len(nums)
        res = [1] * n

        # Pass 1, left to right: res[i] = product of everything LEFT of i
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # Pass 2, right to left: multiply in the product of everything RIGHT of i
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
        return 
