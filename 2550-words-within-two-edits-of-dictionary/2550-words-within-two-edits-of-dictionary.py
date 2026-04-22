class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        i = 0; j = 0; # i for queries, j for dictionary
        len_queries = len(queries); len_dict = len(dictionary)
        result = []
        def check(word,dictionary):
            
            for curr_word in dictionary:
                count = 0
                if len(curr_word)==len(word):
                    for j in range(len(word)):
                        if curr_word[j]!=word[j]:
                            count += 1
                if count <= 2:
                    return True
            return False

        while i < len_queries:
            query_word = queries[i]
            t = check(query_word,dictionary)
            if t:
                result.append(query_word)
            i = i+1
        return result