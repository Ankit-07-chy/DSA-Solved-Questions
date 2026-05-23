class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = []; s2 = []
        for _ in s:
            if _ ==  '#' and s1:
                s1.pop()
            elif _ != '#':
                s1.append(_)
        for _ in t:
            if _ ==  '#' and s2:
                s2.pop()
            elif _ != '#':
                s2.append(_)
        return ''.join(s1) == ''.join(s2)