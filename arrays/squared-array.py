class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        def lookup(num, pivot, A):
            if num <= A[pivot]:
                return pivot
            
            for i in range(pivot, len(A) - 1):
                curr = A[i]
                next = A[i + 1]
                if curr <= num <= next:
                    return i
                
            return len(A) - 1
        
        pivot = len(A) - 1
        for i, num in enumerate(A):
            if num >= 0:
                pivot = i

        i = 0
        while(i < len(A)):
            num = A[i]
            if num >= 0:
                A[i] = num * num
            elif num < 0:
                pos = lookup(-1 * num, pivot, A)
                A.insert(pos, -1 * num)
                del A[i]
                pivot -= 1
                i -= 1

            i += 1

        return A
