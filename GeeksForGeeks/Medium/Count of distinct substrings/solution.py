class Solution:
    def countSubs(self, s):
        
        # code here
        class Trie:
            
            class TrieNode:
                def __init__(self):
                    self.children = {}
            
            def __init__(self):
                self.root = self.TrieNode()
                
        
        trie = Trie()
        count = 0
            
        n = len(s)
        for i in range(0,n):
            curr = trie.root
            for j in range(i,n):
                if s[j] not in curr.children:
                    curr.children[s[j]] = trie.TrieNode()
                    
                    count += 1
                curr = curr.children[s[j]]
        return count