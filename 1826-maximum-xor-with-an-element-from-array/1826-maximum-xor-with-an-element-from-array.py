class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        len_q = len(queries)
        result = [-1]*len_q

        class Trie:
            
            class TrieNode:
                def __init__(self):
                    self.children = {}

            def __init__(self):
                self.root = Trie.TrieNode()
            def insert(self,num):
                bits = format(num,'032b')
                crawl = self.root

                for bit in bits:
                    if bit not in crawl.children:
                        crawl.children[bit] = Trie.TrieNode()
                    crawl = crawl.children[bit]
            
            def check(self,x):
                max_xor = 0
                bits = format(x,'032b')
                crawl = self.root
                for bit in bits:
                    opposite = '1' if bit =='0' else '0'
                    if opposite in crawl.children:
                        crawl = crawl.children[opposite]
                        max_xor = (max_xor << 1) | 1 
                    else:
                        crawl = crawl.children[bit]
                        max_xor = (max_xor << 1) | 0
                return max_xor

        nums.sort()
        queries_ = []
        for i,q in enumerate(queries):
            temp = [q[0],q[1],i]
            queries_.append(temp)
        queries_.sort(key=lambda x: x[1])

        i = 0; n = len(nums)
        trie = Trie()
        for query in queries_:
            x = query[0]; val = query[1]; idx = query[2]

            while i < n and nums[i]<=val:
                trie.insert(nums[i])
                i += 1
            if i > 0:
                result[idx] = trie.check(x)
        return result
        





'''
class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result = []

        class Trie:

            class TrieNode:
                def __init__(self):
                    self.children = {}
                

            def __init__(self):
                self.root = Trie.TrieNode()
            def insert(self,num):
                bits = format(num,'032b')
                crawl = self.root
                for bit in bits:
                    if bit not in crawl.children:
                        crawl.children[bit] = Trie.TrieNode()
                    crawl = crawl.children[bit]
            def check(self,num):
            
                bits = format(num,'032b')
                max_bit = 0
                crawl = self.root

                for bit in bits:
                    opposite = '1' if bit == '0' else '0'
                    if opposite in crawl.children:
                        max_bit = (max_bit<<1) | 1
                        crawl = crawl.children[opposite]
                    else:
                        max_bit = (max_bit<<1) | 0
                        crawl = crawl.children[bit]
                return max_bit
        
        
        for q in queries:
            x = q[0]
            small = q[1]
            

            trie = Trie()
            for num in nums:
                if num <= small:
                    trie.insert(num)

            if not trie.root.children:
                result.append(-1)
            else:
                result.append(trie.check(x))
        return result
'''