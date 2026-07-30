class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        def merge(nums,left,mid,right):
            nonlocal count
            
            i = left; j = mid + 1
            for i in range(left,mid+1):
                while j <= right and nums[i]>2*nums[j]:
                    j += 1
                count =count+ j - mid - 1
                

            i = left
            j = mid + 1
            temp = []

            while i<=mid and j <= right:
                if nums[i]<=nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    # nums[i] > nums[j] --> here we have to check either nums[i]>2*nums[j] --> (mid-i+1)
                    temp.append(nums[j])
                    j += 1
            while i <= mid:
                temp.append(nums[i])
                i += 1
            while j <= right:
                temp.append(nums[j])
                j += 1

            for k in range(len(temp)):
                nums[left+k] = temp[k]

        def divide(nums,left,right):
            if left >= right:
                return
            mid = (left+right)//2

            divide(nums,left,mid)
            divide(nums,mid+1,right)

            merge(nums,left,mid,right)
        divide(nums,0,n-1)
        return count
'''
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # brute force 
        count = 0
        n = len(nums)
        for i in range(0,n):
            for j in range(i+1,n):
                if nums[i]>2*nums[j]:
                    count += 1
        return count
        # o(n**2) -> TC, o(1) -> S.C'''