class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for c in s:
            if (s.count(c) != t.count(c) or len(s) != len(t)):
                return False

            if (c in t):
                continue
            else: 
                return False
        return True
        