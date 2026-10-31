import sys
class Solution(object):
    def uniquePaths(self, grid):
        sys.setrecursionlimit(10**6)
        MOD=10**9+7
        m,n=len(grid),len(grid[0])
        memo=[[[-1,-1] for _ in range(n)] for _ in range(m)]
        def dfs(i,j,d):
            if i>=m or j>=n:
                return 0
            if memo[i][j][d]!=-1:
                return memo[i][j][d]
            if grid[i][j]==1:
                if d==0:
                    res=dfs(i+1,j,1)
                else:
                    res=dfs(i,j+1,0)
            elif i==m-1 and j==n-1:
                res=1
            else:
                res=(dfs(i,j+1,0)+dfs(i+1,j,1))%MOD
            memo[i][j][d]=res
            return res
        if m==1 and n==1:
            return 1
        return (dfs(0,1,0)+dfs(1,0,1))%MOD