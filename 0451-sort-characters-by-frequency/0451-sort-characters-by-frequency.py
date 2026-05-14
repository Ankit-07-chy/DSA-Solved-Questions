class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for _ in s:
            if _ in freq:
                freq[_] += 1
            else:
                freq[_] = 1
        freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        t = []
        for u,v in freq:
            t.append(u*v)
        return ''.join(t)