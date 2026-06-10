class Trie {
    private TrieNode root;

    public class TrieNode{
        private TrieNode[] children;
        private boolean isEndofWord;

        public TrieNode(){
            children = new TrieNode[26];
            isEndofWord = false;
        }
    }

    public Trie() {
        root = new TrieNode();
    }
    
    public void insert(String word) {
        TrieNode crawl = root;

        for(char c: word.toCharArray()){
            int idx = c - 'a';
            if (crawl.children[idx] == null){
                crawl.children[idx] = new TrieNode();
            }
            crawl = crawl.children[idx];
        }
        crawl.isEndofWord = true;
    }
    
    public boolean search(String word) {
        TrieNode crawl = root;
        for (char c: word.toCharArray()){
            int idx = c - 'a';
            if (crawl.children[idx]==null){
                return false;
            }
            crawl = crawl.children[idx];
        }
        return crawl.isEndofWord;
        
    }
    
    public boolean startsWith(String prefix) {
        TrieNode crawl = root;
        for (char c: prefix.toCharArray()){
            int idx = c - 'a';
            if (crawl.children[idx]==null){
                return false;
            }
            crawl = crawl.children[idx];
        }
        return true;
    }
}

/*
class Trie:

    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_end_of_word = False

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = self.TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
*/


/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */