class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        for forward, backward in zip(s, reversed(s)):
            if forward != backward:
                return False
        return True