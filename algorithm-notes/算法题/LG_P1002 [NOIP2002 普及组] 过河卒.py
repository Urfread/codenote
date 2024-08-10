# 1.读入B点坐标，马的坐标
bx,by,hx,hy=map(int,input().split())

# 2.1创建棋盘
chessboard=[[0]*(by+1) for _ in range(bx+1)]
# 2.2记录障碍(注意不要越界)
obstacles=[]
# 2.3偏移量
displacement=[(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
for x,y in displacement:
    if hx+x<0 or hx+x>bx or hy+y<0 or hy+y>by:
        continue
    obstacles.append((hx+x,hy+y))
# 2.4添加障碍
for x,y in obstacles:
    chessboard[x][y]=1

# 遍历方向
directions=[(1,0),(0,1)]
# 寻找路径
def find_path(x,y):
    dp=[[0]*(by+1) for _ in range(bx+1)]
    # 初始化第一列和第一行
    for y in range(by+1):
        if chessboard[0][y] == 1:
            break
        dp[0][y]=1
    for x in range(bx+1):
        if chessboard[x][0] == 1:
            break
        dp[x][0]=1
    
    for x in range(1,bx+1):
        for y in range(1,by+1):
            if chessboard[x][y]==1:
                continue
            dp[x][y]=dp[x-1][y]+dp[x][y-1]
    for line in dp:
        print(line)
    return dp[bx][by]

for line in chessboard:
    print(line)
print()
print(find_path(0,0))