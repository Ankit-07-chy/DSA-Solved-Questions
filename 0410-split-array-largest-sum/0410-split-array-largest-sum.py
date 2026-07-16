class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = min(nums)
        high = sum(nums)
        ans = high

        def check(array,sum_to_be,array_split_no):
            curr_arr_no = 1
            curr_sum = 0

            for num in array:
                if num > sum_to_be:
                    return False
                elif (int(num) + int(curr_sum)) <= sum_to_be:
                    curr_sum += num
                else:
                    curr_sum = num
                    curr_arr_no += 1
            return array_split_no >= curr_arr_no


        while low <= high:
            mid = (low+high)//2

            temp = check(nums,mid,k)
            if temp:
                ans = mid 
                high = mid - 1
            else:
                low = mid + 1

        return ans