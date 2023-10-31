t = int(input())
 
def connect(idx, cnt, length):
    global maxCnt, minLength
 
    if idx == len(cell_list):
        if cnt > maxCnt:
            maxCnt = cnt
            minLength = length
        elif cnt == maxCnt:
            minLength = min(length, minLength)
        return
 
    x, y = cell_list[idx]
 
    for d in range(4):
        count = 0
        nx = x
        ny = y
 
        while True:
            nx += dx[d]
            ny += dy[d]
 
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                break
 
            if cell[nx][ny] == 1:
                count = 0
                break
            count += 1
 
        originX = x
        originY = y
        for _ in range(count):
            originX += dx[d]
            originY += dy[d]
 
            cell[originX][originY] = 1
 
        if count == 0:
            connect(idx+1, cnt, length)
        else:
            connect(idx+1, cnt+1, length+count)
 
            originX = x
            originY = y
 
            for _ in range(count):
                originX += dx[d]
                originY += dy[d]
 
                cell[originX][originY] = 0
 
 
for tc in range(1, t+1):
 
    n = int(input())
 
    cell = [list(map(int, input().split())) for _ in range(n)]
 
    cell_list = []
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                continue
            if cell[i][j] == 1:
                cell_list.append((i, j))
 
    maxCnt = 0
    minLength = 9999
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
 
    connect(0, 0, 0)
 
    print("#{} {}".format(tc, minLength))
