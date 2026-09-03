class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        n = len(candidates)

        def recursion(idx,stack,target):
            if target == 0:
                result.append(stack[:])
                return 
            elif target < 0:
                return 
            elif idx >= n:
                return 
            else:
                stack.append(candidates[idx])
                pick = recursion(idx+1,stack,target-stack[-1])
                t = stack.pop()
                j = idx
                while j < n and candidates[j] == t:
                    j += 1
                not_pick = recursion(j,stack,target)
        recursion(0,[],target)
        return result
