class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Naive
        seen = []
        sub = []
        for i, word in enumerate(strs):
            wrd_sorted = "".join(sorted(word))
            if wrd_sorted in seen:
                sub[seen.index(wrd_sorted)].append(word)
            else:
                seen.append(wrd_sorted)
                sub.append([])
                sub[seen.index(wrd_sorted)].append(word)
        return sub

        
        #
