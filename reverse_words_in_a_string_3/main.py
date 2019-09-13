class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(" ")
        
        # solution 1
        # l = ["".join(reversed(i)) for i in l]
        # return " ".join(l)
        
        # solution 2
        for i in range(len(l)):
            l[i] = "".join(reversed(l[i]))
        return " ".join(l)
