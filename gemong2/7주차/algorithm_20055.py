N, K = map(int, input().split())

arr = list(map(int, input().split()))
zerocnt = 0
box = [0]*(2*N)
front = 0
rear = 2*N - 1
down = N - 1
cnt = 0
while zerocnt < K:
    front -= 1
    rear -= 1
    down -= 1
    if front == -1:
        front = 2*N - 1
    elif rear == -1:
        rear = 2*N - 1
    if down == -1:
        down = 2*N - 1
    for i in range(2*N):
        if box[i] == 1:
            if i == 2*N-1:
                if box[0] == 0 and arr[0] != 0:
                    box[i], box[0] = box[0], box[i]
                    arr[0] -= 1
                    if arr[0] == 0:
                        zerocnt += 1
                    if down == 0:
                        box[0] = 0

            else:
                if box[i+1] == 0 and arr[i+1] != 0:
                    box[i], box[i+1] = box[i+1], box[i]
                    arr[i+1] -= 1
                    if arr[i+1] == 0:
                        zerocnt += 1
                    if down == i+1:
                        box[i+1] = 0
    if box[front] == 0 and arr[front] != 0:
        box[front] = 1
        arr[front] -= 1
        if arr[front] == 0:
            zerocnt += 1
    cnt += 1

print(cnt)
