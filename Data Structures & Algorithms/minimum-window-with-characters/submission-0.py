class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Shortest so variable window size.
        # Assume correct output is always unique.
        if not t or not s:
            return ""
        need = Counter(t)
        window = Counter()
        have, needed = 0, len(need)
        start = 0
        best = (float("inf"), 0, 0)

        for end, char in enumerate(s):
            window[char] += 1
            if char in need and window[char] == need[char]:
                have += 1
            while have == needed:                      
                if end - start + 1 < best[0]:
                    best = (end - start + 1, start, end)
                window[s[start]] -= 1
                if s[start] in need and window[s[start]] < need[s[start]]:
                    have -= 1
                start += 1

        return "" if best[0] == float("inf") else s[best[1]:best[2] + 1]