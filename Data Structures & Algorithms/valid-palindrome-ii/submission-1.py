class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        char_deleted = False
        while l < r:
            if char_deleted and s[l] != s[r]:
                return False
    
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                char_deleted = True
                if s[l+1] == s[r] and s[l] != s[r-1]: 
                    l += 1
                else:
                    r -= 1
        return True