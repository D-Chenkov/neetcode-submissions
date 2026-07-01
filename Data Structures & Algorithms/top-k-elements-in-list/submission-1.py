class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #naive
        print(Counter(nums))
        skt = list(Counter(nums).most_common())
        print(skt)
        res = []
        for i in range(k):
            res.append(skt[i][0])
        return(list(res))
