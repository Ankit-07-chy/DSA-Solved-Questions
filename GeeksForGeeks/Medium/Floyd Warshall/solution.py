class Solution:
	def floydWarshall(self, dist):
		#Code here
		
		n = len(dist)
		for via in range(0,n):
		    for i in range(0,n):
		        for j in range(0,n):
		            if (dist[i][via] != 10**8 and
                        dist[via][j] != 10**8 and
                        dist[i][via] + dist[via][j] < dist[i][j]):

                        dist[i][j] = dist[i][via] + dist[via][j]
		return dist