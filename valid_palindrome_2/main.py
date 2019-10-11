class Solution:
    def isPalindrome(self, s: str) -> (bool, int, int):
        hi = len(s) - 1
        mid = hi / 2
        
        for lo, char_lo in enumerate(s):
            if lo >= mid:
                break

            char_hi = s[hi]

            if char_lo == char_hi:
                hi -= 1
                continue
            else:
                return (False, lo, hi)

        return (True, lo, hi)
    
    def validPalindrome(self, s: str) -> bool:
        res, lo, hi = self.isPalindrome(s)

        if not res:
            sub = s[lo+1:hi+1]
            res, _, _ = self.isPalindrome(sub)
            
        if not res:
            sub = s[lo:hi]
            res, _, _ = self.isPalindrome(sub)
        
        return res
