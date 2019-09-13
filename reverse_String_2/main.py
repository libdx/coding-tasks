class Solution:
    def _reverseFirstKIn2KRange(self, s: str, k: int) -> str:
            sub_str1 = s[:k]
            sub_str2 = s[k:2 * k]

            sub_str1 = "".join(reversed(sub_str1))
            
            return sub_str1 + sub_str2
            
    
    def reverseStr(self, s: str, k: int) -> str:
        str_len = len(s)
        
        res = ""
        step = 2 * k
        for i in range(0, str_len, step):
            sub_str = s[i: i + step]
            sub_str = self._reverseFirstKIn2KRange(sub_str, k)
            res += sub_str
        
        return res
