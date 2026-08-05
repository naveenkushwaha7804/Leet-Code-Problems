class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(perm,options):
            if len(perm) == len(nums):
                result.append(perm[:])
                return
            for i in range(len(options)):
                perm.append(options[i])
                backtrack(perm , options[:i] + options[i+1:])
                perm.pop()
        backtrack([],nums)
        return result
        