class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = [c.lower() for c in s if c.isalnum()]
        for i in range (len(cleaned) // 2):
            if cleaned[i] != cleaned[len(cleaned)-1 - i]: 
                return False
        return True
            