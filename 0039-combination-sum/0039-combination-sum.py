class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []; n = len(candidates)
        def recursion(idx,stack,target):
            if idx >= n:
                return
            if target == 0:
                result.append(stack[:])
                return
            # pick
            if target >= candidates[idx]:
                stack.append(candidates[idx])
                recursion(idx,stack,target-candidates[idx])
                stack.pop()
            recursion(idx+1,stack,target)
        recursion(0,[],target)
        return result