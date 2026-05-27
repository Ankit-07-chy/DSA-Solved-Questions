class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        n = len(word)
        low = [[] for _ in range(26)]
        high = [float('inf')]*26
        for idx,val in enumerate(word):
            temp = ord(val)
            if 65<=temp<=90:
                high[temp-65] = min(high[temp-65],idx)
            else:
                low[temp-97].append(idx)
        count = 0
        for l1, val in list(zip(low,high)):
            if l1:
                temp = True
            
                for e in l1 :
                    if e > val:
                        temp = False
                        break
                if temp and val != float('inf'):
                    count += 1
        return count
# Brute Force
'''
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        n = len(word)
        visited = [0]*(n)
        freq = {} # key, [idx]
        for idx,val in enumerate(word):
            if val in freq:
                freq[val].append(idx)
            else:
                freq[val] = [idx]
        count = 0
        low, high = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        for char1, char2 in list(zip(low,high)):
            if char1 in freq and char2 in freq:
                list1,list2 = freq[char1],freq[char2]
                if list1 and list2:
                    temp = True
                    for e in list1:
                        if e > list2[0]:
                            temp = False
                    if temp:
                        count += 1
        return count
'''