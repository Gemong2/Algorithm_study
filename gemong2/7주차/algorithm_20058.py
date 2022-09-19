N, Q = map(int, input().split())

arr = [0]*(2**N)
for i in range(2**N):
    arr[i] = list(map(int, input().split()))
