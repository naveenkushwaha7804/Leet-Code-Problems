class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def backtrack(comb,start):
            if len(comb) == k:
                result.append(comb[:])
                return 
            for i in range(start,n+1):
                comb.append(i)
                backtrack(comb,i+1)
                comb.pop()
        backtrack([],1)
        return result
