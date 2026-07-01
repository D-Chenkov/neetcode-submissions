class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Its the complement trick again
        for i, num in enumerate(numbers):
            if (target-num in numbers):
                print(i)
                print(num)
                return [i+1, numbers.index(target-num)+1]
        return False