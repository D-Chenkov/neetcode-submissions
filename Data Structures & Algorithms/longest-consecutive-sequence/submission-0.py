class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        cumax = 0
        for num in nset:
            if (num-1) not in nset: 
                curr_count = 1
                curr_num = num
                while(curr_num+1 in nset):
                    curr_count += 1
                    curr_num +=1
                cumax = max(cumax, curr_count)

        return cumax
        