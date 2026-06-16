class Solution:
	def subsetSums(self, arr):
		# code here
		result = []
		n = len(arr)
		def recursion(idx,sumi):
		    if idx >= n:
		        result.append(sumi)
		        return # base case
		    
		    recursion(idx+1,sumi+arr[idx])
		    recursion(idx+1,sumi)
		recursion(0,0)
		result.sort()
		return result