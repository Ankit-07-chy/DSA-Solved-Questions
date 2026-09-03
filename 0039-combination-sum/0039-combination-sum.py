class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        result = []
        def recursion(idx,stack,k):
            if k == 0:
                result.append(stack[:])
                return 
            elif idx >= n:
                return 
            else:
                pick = 0
                if k >= candidates[idx]:
                    stack.append(candidates[idx])
                    pick = recursion(idx,stack,k-candidates[idx])
                    stack.pop()
                not_pick = recursion(idx+1,stack,k)
        recursion(0,[],target)
        return result
