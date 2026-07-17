class Solution:
    def rowWithMax1s(self, arr):
        ans_idx = -1
        ans = 0
        def check(row):
            low = 0
            high = len(row) - 1
            first = len(row)
        
            while low <= high:
                mid = (low + high) // 2
        
                if row[mid] == 1:
                    first = mid
                    high = mid - 1
                else:
                    low = mid + 1
        
            return len(row) - first

        # def check(row):
        #     low = 0
        #     high = len(row) - 1

        #     curr = 0
        #     if row[low] == row[high] == 0:
        #         return 0
        #     if row[low] == 1:
        #         return high + 1

        #     while low <= high:
        #         mid = (low + high) // 2

        #         if row[low] == 1:
        #             return high + 1 - low

        #         if row[mid] == 1:
        #             curr = high - mid + 1
        #             high = mid - 1
        #         else:
        #             low = mid + 1

        #     return curr

        for idx, row in enumerate(arr):
            temp = check(row)
            if temp > ans:
                ans = temp
                ans_idx = idx

        return ans_idx