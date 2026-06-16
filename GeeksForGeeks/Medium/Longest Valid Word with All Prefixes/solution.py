class Solution:
    def longestValidWord(self, words):
        # code here 
        
        class Trie:
            class TrieNode:
                def __init__(self):
                    self.children = {}
                    self.isEnd = False
            
            def __init__(self):
                self.root = Trie.TrieNode()
            def insert(self,word):
                crawl = self.root
                for char in word:
                    if char not in crawl.children:
                        crawl.children[char] = Trie.TrieNode()
                    crawl = crawl.children[char]
                crawl.isEnd = True
        
        
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        def check_(word):
            curr = trie.root
            for c in word:
                if c not in curr.children:
                    return False
                curr = curr.children[c]
                if not curr.isEnd:
                    return False
            return True
                
        longest_word = ''

        for word in words:
            if check_(word):
                if len(word) > len(longest_word):
                    longest_word = word
                elif len(word) == len(longest_word):
                    longest_word = min(longest_word, word)
        
        return longest_word