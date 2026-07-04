class Solution:
	def nextSmallerEle(self, arr):
		# code here
		n = len(arr)
		ans = [-1]*n
		
		# monotonic inc stack
		stack = []
		i = n-1
		while i >= 0:
		    while stack and stack[-1]>=arr[i]:
		        stack.pop()
	        if not stack:
	            ans[i] = -1
	        else:
	            ans[i] = stack[-1]
	        stack.append(arr[i])
		    
		    
		    i-=1
		return ans