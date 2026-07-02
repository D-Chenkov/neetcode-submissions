class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        trips = []
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    trips.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        trips =  set(tuple(t) for t in trips)
        return list(trips)  
        ##Starting off from 2sum   
        #l = 0
        #r = len(numbers)-1
        #m = 1
        #while l < r:
        #    s = numbers[l] + numbers[r]
        #    if target == s:
        #        return [l+1, r+1]
        #    elif s < target:
        #        l+=1
        #    else:
        #        r-=1
        #return []

