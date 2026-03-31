class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        s = ["a"] * (n + m - 1)
        fixed = [False] * (n + m - 1)

        # process the case of 'T'
        for i, ch in enumerate(str1):
            if ch == "T":
                for j, c in enumerate(str2, i):
                    if fixed[j] and s[j] != c:
                        return ""
                    s[j], fixed[j] = c, True

        # process the case of 'F'
        for i, ch in enumerate(str1):
            if ch == "F":
                # check if there are already different characters
                if any(str2[j - i] != s[j] for j in range(i, i + m)):
                    continue

                # find the first modifiable position
                for j in range(i + m - 1, i - 1, -1):
                    if not fixed[j]:
                        s[j] = "b"
                        break
                else:
                    return ""

        return "".join(s)
'''
class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n = len(str1); m = len(str2)
        ans = [0]*(n+m-1)
        for i in range(n):
            if str1[i] == 'T':
                temp = i
                for u in str2:
                    ans[temp] = u
                    temp += 1
            else:
                if ans[i] == 0:
                    ans[i] = 'a'
        for i in range(n):
            if str1[i] == 'T':
                temp = i
                for u in str2:
                    if ans[temp] != u:
                        return ''
                    temp += 1
        for i in range(n+m-1):
            if ans[i] == 0:
                ans[i] = 'a'
        return ''.join(ans)
        ''' '''
        n = len(str1); m = len(str2)
        # word has length of n-m+1; str1 contains only TFTF and str2 contains lower alphabatical chars
        ans = [0]*(n+m-1)
        # print(ans)
        for i in range(n):
            if str1[i] == 'T' and ans[i] == 0:
                # print('i', i)
                # write main logic here
                temp = i
                for u in str2:
                    ans[temp] = u
                    temp += 1
            elif str1[i] == 'T' and ans[i] != 0 :
                # another logic
                temp = i
                for u in str2:
                    if u != ans[temp] and ans[temp] != 0:
                        return ''
                    elif u != ans[i] and ans[i] == 0:
                        ans[temp] = u
                    else: # u == ans[i] then check for rest str2 element
                        for te in range(1,m):
                            if ans[temp+te] != str2[te] and ans[temp+te] != 0:
                                return ''
                            else:
                                ans[temp+te] = str2[te]
                        break
                    temp += 1
            else:
                ans[i]='a'
                    
        for i in range(n+m-1):
            if ans[i] == 0:
                ans[i] = 'a'
        return ''.join(ans)
        '''