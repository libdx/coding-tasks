class Solution:
    def isPalindrome(self, s: str) -> bool:
        lo = 0
        hi = len(s) - 1
        mid = hi / 2
        
        while lo < mid:
            lo_char = s[lo]
            hi_char = s[hi]

            while not lo_char.isalnum():
                lo += 1
                lo_char = s[lo]
                if lo >= mid:
                    break
            
            while not hi_char.isalnum():
                hi -= 1
                hi_char = s[hi]
                if hi <= mid:
                    break

            if not all([lo_char.isalnum(), hi_char.isalnum()]):
                # String or sub-string with non-alphanumeric characters to be palindrome
                return True

            if lo_char.lower() == hi_char.lower():
                lo += 1
                hi -= 1
                continue
            else:
                return False

        return True
