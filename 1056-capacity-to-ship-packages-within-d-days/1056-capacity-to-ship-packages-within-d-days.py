class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights); high = sum(weights)

        if high == 0:
            return -1

        # weights.sort()

        ans = high

        def check(arr,days,capacity):
            count = 1
            curr_cap = 0
            n = len(arr)
          
            for i in range(0,n):
                curr_cap += arr[i]
                if curr_cap > capacity:
                    count += 1
                    curr_cap = arr[i]

            return count <= days



        while low <= high:
            mid = (low + high)//2
            t = check(weights,days,mid)
            if t==True:
                ans = mid 
                high = mid - 1
            else:
                low = mid + 1
        return ans
