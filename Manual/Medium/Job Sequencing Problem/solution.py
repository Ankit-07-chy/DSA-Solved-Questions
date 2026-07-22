class Solution:
    def jobSequencing(self, deadline, profit):
        # code here
        list1 = list(zip(deadline,profit))
        list1.sort(key = lambda x: x[1],reverse=True)
        # print(list1)
        n = 0
        for d in deadline:
            n = max(d,n)
        
        count_profit = 0; count_process = 0
        indexes = [-1]*(n+1)
        for u,v in list1:
            # u-> deadline, v -> profit
            if indexes[u] == -1:
                count_profit += v
                indexes[u] = v
                count_process += 1
            else:
                for idx in range(u,0,-1):
                    if indexes[idx] == -1:
                        count_profit += v
                        indexes[idx] = v
                        count_process += 1
                        break
        return count_process,count_profit
            