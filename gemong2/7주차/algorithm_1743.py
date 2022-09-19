import sys
sys.setrecursionlimit(10**6)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(i, j):
    visited[i][j] = 1
    global maxtrash
    maxtrash += 1
    for turn in range(4):
        ai = i + dx[turn]
        aj = j + dy[turn]
        if 0 <= ai < N and 0 <= aj < M and visited[ai][aj] == 0 and arr[ai][aj] == 1:
            dfs(ai, aj)


N, M, K = map(int, input().split())


arr = [[0]*M for _ in range(N)]

for i in range(K):
    x, y = map(int, input().split())

    arr[x-1][y-1] = 1

visited = [[0]*M for _ in range(N)]


trash = 0

for a in range(N):
    for b in range(M):
        if arr[a][b] == 1 and visited[a][b] == 0:
            maxtrash = 0
            dfs(a, b)
            trash = max(maxtrash, trash)

print(trash)


# q = []
# def bfs(i, j):
#     global maxtrash
#     q.append([i, j])
#     visited[i][j] = True
#     maxtrash += 1

#     while q:
#         i, j = q[0][0], q[0][1]
#         del q[0]

#         for k in range(4):
#             ai = i + dx[k]
#             aj = j + dy[k]

#             if 0 <= ai < N and 0 <= aj < M and not visited[ai][aj] and arr[ai][aj] == 1:
#                 q.append([ai, aj])
#                 visited[ai][aj] = True
#                 maxtrash += 1
