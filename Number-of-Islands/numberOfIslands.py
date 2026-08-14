class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        rows = len(grid)
        cols = len(grid[0])
        def transform(r,c):
            grid[r][c] = '0'
            q = deque()
            q.append((r,c))
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            while q:
                row, col = q.popleft()
                for dr,dc in directions:
                    nr,nc=dr+row,dc+col
                    if nr<0 or nc<0 or nr>=rows or nc>=cols or grid[nr][nc]!='1':
                        continue
                    q.append((nr,nc))
                    grid[nr][nc]='0'             
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    island +=1
                    transform(r,c)
        return island

        