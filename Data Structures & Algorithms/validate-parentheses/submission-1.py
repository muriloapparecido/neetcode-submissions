class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        pairs = {"(":")", "{":"}", "[": "]"}
        for c in s: 
            if c in "([{":
                seen.append(c)
            else: 
                if not seen or pairs[seen[-1]] != c:
                    return False
                seen.pop()
        return len(seen) == 0
            