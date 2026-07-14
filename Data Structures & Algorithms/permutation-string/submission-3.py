class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #Naive and SLOW
        #I hadn't understood that it needs to check for CAB not C_AB
        #def get_permutations(s):
        #    if len(s) <= 1:
        #        return [s]
        #    
        #    variants = []
        #    for i, char in enumerate(s):
        #        remaining = s[:i] + s[i+1:]
        #        for perm in get_permutations(remaining):
        #            variants.append(char + perm)       
        #    return variants
        #s1_perms = get_permutations(s1)
        #return any(element in s2 for element in s1_perms)


        if len(s1) > len(s2):
            return False

        #Traverse the array with the window size
        #Add the element when you slide, and remove the last element
        idealCount = Counter(s1)
        windowCount = Counter()
        windowSize = len(s1)
        start = 0

        for end, incoming in enumerate(s2):
            windowCount[incoming]+=1
            if end - start + 1 == windowSize:
                if windowCount == idealCount:
                    return True
                outgoing = s2[start]
                windowCount[outgoing] -= 1
                if windowCount[outgoing] == 0:
                    del windowCount[outgoing]
                start+=1
                
            
        return False
            

