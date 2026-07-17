class Solution:
	def matSearch(self, mat, x):
		# code here
		i = 0; j = len(mat[0])-1
		rows = len(mat); cols = len(mat[0])
		while True:
		    if i>=rows or i < 0 or j < 0 or j >= cols:
		        return False
		  
		    elif mat[i][j] == x:
		        return True
		    elif mat[i][j]<x:
		        i += 1
		    elif mat[i][j]>x:
		        j -= 1