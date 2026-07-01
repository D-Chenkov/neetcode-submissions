class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Always
        if len(s) != len(t):
            return False
        #Sorting
        return sorted(s) == sorted(t)
        
        #Hashing
        return Counter(s) == Counter(t)

        #
        #if set(s) == set(t):
        #    return True
        #return False