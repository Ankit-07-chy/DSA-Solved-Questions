class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        
        n = len(stones)
        mapp = {}
        for idx,val in enumerate(stones):
            mapp[val] = idx

        dp = {}
        
        def recursion(curr_pos_idx, jump):
            if curr_pos_idx == n-1:
                return True
            elif curr_pos_idx >= n:
                return False
            
            if (curr_pos_idx,jump) in dp:
                return dp[(curr_pos_idx,jump)]

            one = jump - 1
            two = jump
            three = jump + 1
            t1 = False; t2 = False; t3 = False
            if one > 0 and stones[curr_pos_idx] + one in mapp:
                next_idx = mapp[stones[curr_pos_idx] + one]
                if (next_idx,one) not in dp:
                    
                    dp[(next_idx,one)] = recursion(next_idx,one)
                t1 = dp[(next_idx,one)]
            if stones[curr_pos_idx] + two in mapp:
                next_idx = mapp[stones[curr_pos_idx] + two]
                if (next_idx, two) not in dp:
                    dp[(next_idx, two)] = recursion(next_idx, two)
                t2 = dp[(next_idx, two)]
            if stones[curr_pos_idx] + three in mapp:
                next_idx = mapp[stones[curr_pos_idx] + three]
                if (next_idx, three) not in dp:
                    dp[(next_idx, three)] = recursion(next_idx,three)
                t3 = dp[(next_idx,three)] 

            dp[(curr_pos_idx,jump)] = t1 or t2 or t3
            return dp[(curr_pos_idx,jump)]
        return recursion(1,1)
