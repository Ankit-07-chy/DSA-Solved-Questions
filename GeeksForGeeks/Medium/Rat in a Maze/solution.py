class Solution:
    def ratInMaze(self, maze: list[list[int]]) -> list[str]:
        # code here
        ans = []
        n = len(maze)
        
        if maze[0][0] == 0 or maze[-1][-1] == 0:
            return []
        
        def fxn(i,j,stack):
            if i == n-1 and j == n-1:
                ans.append(''.join(stack))
                return 
            elif i > n-1 or j > n-1:
                return 
            else:
                if i+1<n and maze[i+1][j] == 1 and visited[i+1][j] == False:
                    stack.append('D')
                    visited[i+1][j] = True
                    fxn(i+1,j,stack)
                    visited[i+1][j] = False
                    stack.pop()
                if j+1<n and maze[i][j+1] == 1 and visited[i][j+1] == False:
                    visited[i][j+1] = True
                    stack.append('R')
                    fxn(i,j+1,stack)
                    visited[i][j+1] = False
                    stack.pop()
                if i-1 >=0 and maze[i-1][j] == 1 and visited[i-1][j] == False:
                    visited[i-1][j] = True
                    stack.append('U')
                    fxn(i-1,j,stack)
                    visited[i-1][j] = False
                    stack.pop()
                if j-1 >=0 and maze[i][j-1] == 1 and visited[i][j-1] == False:
                    visited[i][j-1] = True
                    stack.append('L')
                    fxn(i,j-1,stack)
                    visited[i][j-1] = False
                    stack.pop()
                    
                return 
        visited = [[False]*n for _ in range(n)]
        visited[0][0] = True
        fxn(0,0,[])
        return sorted(ans)
                