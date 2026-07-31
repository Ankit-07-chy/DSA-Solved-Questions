class Solution:
    def minimumPushes(self, word: str) -> int:
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

