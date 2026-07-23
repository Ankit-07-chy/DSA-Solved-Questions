class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        #code here
        
        new_list = []
        for v,w in zip(val,wt):
            new_list.append([v,w])
            
        new_list.sort(key = lambda x:x[0]/(x[1]+0.000000001),reverse= True)
        ans = 0
        for i in range(len(val)):
            v,w = new_list[i]
            if capacity == 0:
                return ans
            if w <= capacity:
                capacity -= w
                ans += v 
            elif w > capacity:
                frac = (capacity/w)
                ans += (v*frac)
                
                capacity = 0
                
        return ans
            