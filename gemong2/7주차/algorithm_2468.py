import sys
sys.setrecursionlimit(10**6)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(i, j, high):
    for turn in range(4):
        ai = i + dx[turn]
        aj = j + dy[turn]

        if 0 <= ai < N and 0 <= aj < N and not visited[ai][aj] and arr[ai][aj] > high:
            visited[ai][aj] = True
            dfs(ai, aj, high)


N = int(input())
arr = [0]*N
for k in range(N):
    arr[k] = list(map(int, input().split()))
minarr = min(map(min, arr))
maxarr = max(map(max, arr))

land = 1
for l in range(minarr, maxarr):
    visited = [[False]*N for _ in range(N)]
    maxland = 0
    for p in range(N):
        for q in range(N):
            if arr[p][q] > l and not visited[p][q]:
                maxland += 1
                visited[p][q] = True
                dfs(p, q, l)

    if land < maxland:
        land = maxland

print(land)
