class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        prev = 0; next = 0
        maxLen = 0
        freq = {}
        for next in range(0,len(fruits)):
            if len(freq)<= 2:
                if fruits[next] in freq:
                    freq[fruits[next]]+=1
                else:
                    freq[fruits[next]] = 1
            
            else:
                while len(freq)>2:
                    freq[fruits[prev]]-=1
                    prev += 1
                    if freq[fruits[prev-1]] == 0:
                        freq.pop(fruits[prev-1])
                if fruits[next] in freq:
                    freq[fruits[next]]+=1
                else:
                    freq[fruits[next]] = 1


            if len(freq)<=2:
                maxLen = max(next-prev+1,maxLen)
        return maxLen
