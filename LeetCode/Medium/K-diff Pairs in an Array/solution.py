class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        freq_map = {}
        n = len(nums)
        nums.sort()

        def search(nums,ele,start,end):
            if start > end:
                return False

            while start <= end:
                mid = (start+end)//2
                if nums[mid] == ele:
                    return True
                elif nums[mid]>ele:
                    end = mid - 1
                else:
                    start = mid + 1

            return False

        for i in range(0,n):
            ele_j = k + nums[i]

            # now binary search for ele_j as we know my nums is sorted
            temp = search(nums,ele_j,i+1,n-1) # that element is definetly above this starting one
            if temp:
                freq_map[(nums[i],ele_j)] = freq_map.get((nums[i],ele_j),0) + 1

        return len(freq_map)