class Solution:
    def reverseWords(self, s: str) -> str:
        # s = s[::-1]
        s = s.strip()
        s = s.split(' ')
        t = []
        print(s)
        for _ in s:
            if _ != '':
                
                t.append(_.strip())
        t = t[::-1]
        return ' '.join(t)