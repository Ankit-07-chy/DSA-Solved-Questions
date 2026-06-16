class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        class Trie:
            class TrieNode:
                def __init__(self):
                    self.children = {}

            def __init__(self):
                self.root = Trie.TrieNode()
            
            def insert(self,number):
                number = format(number,'032b')
                crawl = self.root
                for i in number:
                    if i not in crawl.children:
                        crawl.children[i] = Trie.TrieNode()
                    crawl = crawl.children[i]

        trie = Trie()
        for num in nums:
            trie.insert(num)

        def check(num,trie):
            crawl = trie.root
            num = format(num,'032b')
            max_xor = 0
            for c in num:

                # always check for opposite, if yes then choose that and by that flow in that path only
                opposite = '1' if c == '0' else '0'
                if opposite in crawl.children:
                    max_xor = (max_xor<<1) | 1
                    crawl = crawl.children[opposite]
                else:
                    max_xor = (max_xor<<1) | 0
                    crawl = crawl.children[c]
            return max_xor


        maxi = 0
        for num in nums:
            t = check(num,trie) # this will return the element with max
            maxi = max(maxi,t)
        return maxi 






# O(n^2) will give TLE
'''
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        maxi = -inf
        n = len(nums)
        for i in range(0,n):
            for j in range(0,n):
                if i != j:
                    maxi = max(maxi,nums[i]^nums[j])
        return maxi'''