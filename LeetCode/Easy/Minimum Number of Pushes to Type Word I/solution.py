class Solution:
    def minimumPushes(self, word: str) -> int:
        '''
        x -> 1 : 2
        y -> 1 : 3
        c -> 1 : 4
        d -> 1 : 5
        e -> 1 : 6
        f -> 1 : 7
        g -> 1 : 8
        h -> 1 : 9
        i -> 1 : 2
        j -> 1 : 3
        ''' # 12
        # one approach that is coming to mind right now is , inside a map store each single char freq or we know that this is only smaller chars a-z so we can store it to [26] array -> o(n)
        # then i can sort it that will take -> 26ln(26)
        # then assign each map chars to [2-9] and take count also from there -> will take O(26)

        freq_map = {}
        for char in word:
            freq_map[char] = freq_map.get(char,0)+1
        freq_map = dict(sorted(freq_map.items(),key=lambda x:x[-1],reverse=True))
        count = 0

        char_mapping = {}; idx = 2 # 2-3-4----9---9-8-7--------2
        for u,v in freq_map.items():
            char = u
            repeat = v

            if idx > 9:
                idx = 2
            
            if idx not in char_mapping:
                char_mapping[idx] = [char]
                count += (repeat)
            elif idx in char_mapping:
                char_mapping[idx].append(char)
                count += (repeat*len(char_mapping[idx]))
            
            idx += 1

        return count

