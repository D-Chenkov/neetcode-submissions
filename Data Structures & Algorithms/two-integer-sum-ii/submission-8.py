class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Its the complement trick again

        #Same as before but its SORTED now so need to correct from N^2
        #for i, num in enumerate(numbers):
        #    if (target-num in numbers):
        #        return [i+1, numbers.index(target-num)+1]
        #return False

        #Using pointers
        l = 0
        r = len(numbers)-1

        while l < r:
            print(l, r, target)
            if target == numbers[l] + numbers[r]:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] < target:
                l+=1
            else:
                r-=1
        return ["woops", "All errors!"]

                