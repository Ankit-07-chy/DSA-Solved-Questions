class Solution:
    def reverseParentheses(self, s: str) -> str:
        ans = []
        prev_idx = []
        count =0
        for i in range(len(s)):
            if s[i] == '(':
                prev_idx.append(i-count)
                count += 1
            elif s[i] == ')':
                temp = prev_idx.pop()
                ans[temp:] = ans[temp:][::-1]
                count += 1
            else:
                ans.append(s[i])
        return ''.join(ans)

        ''' co -> etco => octe; edocteel : leetcode '''