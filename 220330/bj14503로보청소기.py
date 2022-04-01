import sys

m,n = map(int,sys.stdin.readline().split())
r,c,d = map(int,sys.stdin.readline().split())
arr = []

for i in range(m):
  arr.append(list(map(int,sys.stdin.readline().split())))


  
#북 동 남 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]


x, y = r,c
arr[x][y]=2 
cnt = 1

# d 0,3,2,1 북 서 남 동  회전
def left():
  global d
  d -= 1
  if d == -1:
    d = 3


while 1:

  flag = False
  
  for _ in range(4):
    
    left()
    nx = x + dx[d]
    ny = y + dy[d]
    
    if 0<= nx <m and 0<= ny < n: # nx,ny가 arr벗어나지 않는경우
      if arr[nx][ny]== 0:
        cnt +=1
        arr[nx][ny]=2
        x,y = nx, ny
        flag = True    #방문했으면 flag True
        break
        
  if not flag:  #모든공간 청소 못하는 경우
    
    nx = x - dx[d]
    ny = y - dy[d]
    
    if 0 <= nx < m and 0<= ny < n: # nx,ny 그래프 안에 있을때
      if arr[nx][ny] == 2:
        x,y = nx,ny # 후진
      elif arr[nx][ny] == 1:
        print(cnt)
        break
    else:
      print(cnt)
      break
      
        
print(arr)