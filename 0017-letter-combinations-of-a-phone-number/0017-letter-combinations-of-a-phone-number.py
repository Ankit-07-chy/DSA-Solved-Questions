class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {
            '2':['a','b','c'],
            '3' : ['d','e','f'],
            '4' : ['g','h','i'],
            '5' : ['j','k','l'],
            '6' : ['m','n','o'],
            '7' : ['p','q','r','s'],
            '8' : ['t','u','v'],
            '9':['w','x','y','z']
        }
        ans = []

        n1 = len(digits)

        def recursion(idx,stack):
            if idx >= n1:
                ans.append(''.join(stack))
                return
            
            for j in range(0,len(map[digits[idx]])):
                stack.append(map[digits[idx]][j])
                recursion(idx+1,stack)
                stack.pop()

            return 
        recursion(0,[])
        return ans
