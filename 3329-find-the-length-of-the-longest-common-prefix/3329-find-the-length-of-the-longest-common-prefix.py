class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        lt = 0
        seen = set()
        n1 = len(arr1)
        for i in range(n1):
            num = str(arr1[i])
            s = ''
            for _ in num:
                s = s+_
                seen.add(s)
        for i in range(len(arr2)):
            num = str(arr2[i])
            s = ''
            for _ in num:
                s = s+ _
                if s in seen:
                    lt = max(lt,len(s))
        return lt

        '''
        # m*n(min_word_len) -> T.C

        def find(a,b):
            
        for num1 in arr1:
            curr = 0
            for num2 in arr2:
                curr = find(num1,num2)
            lt = max(lt,curr)
        return lt
'''