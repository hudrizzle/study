import collections
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R, C = len(grid), len(grid[0])
        Q = collections.deque([])
        count = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    Q.append((r,c))
                if grid[r][c] == 1:
                    count += 1

        def neighbors(i, j):
            near_list = []
            for r, c in ((i-1, j), (i, j-1), (i+1, j), (i, j+1)):
                if (0<= r < R) and (0 <= c < C):
                    near_list.append((r, c))
            return near_list

        # BFS
        # print neighbors(0,0)
        num_iter = 0
        # rot_count = 0
        while Q:
            num_iter +=1
            print Q
            for _ in range(len(Q)):
                i, j = Q.popleft()
                for ni, nj in neighbors(i, j):
                    if grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        count -= 1
                        Q.append((ni, nj))
        print count
        if count == 0:
            return num_iter
        else:
            return -1

check = Solution()
grid = [[2,1,1],[1,1,0],[0,1,1]]
res = check.orangesRotting(grid)
print res
