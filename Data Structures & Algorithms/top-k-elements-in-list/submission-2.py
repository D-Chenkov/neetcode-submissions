class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #naive
        skt = list(Counter(nums).most_common(k))
        res= [tup[0] for tup in skt]
        return(res)

        #Bucket


