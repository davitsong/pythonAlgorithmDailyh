import sys
import copy

sys.setrecursionlimit(10**7)

input = sys.stdin.readline

m,n = map(int,input().split())

graph = []
s_arr = []

for _ in range(m):
  graph.append(list(map(int,input().split())))

#상하좌우

dx = [-1,1,0,0]
dy = [0,0,-1,1]




#graph2 = copy.deepcopy(graph)

def bfs(x,y,graph2):
  
  global cnt
  global sum
  global a
  
  
  a = graph2[x][y]
  sum += graph2[x][y]
  graph2[x][y]=0
  cnt += 1

  if(cnt == 4):
    s_arr.append(sum)
    print(sum,x,y)
    return
    
  else:
    
      # 모든영역 check
    for i in range(4):
      
      nx = x + dx[i]
      ny = y + dy[i]
      
    
      if(0<=nx<m and 0<=ny<n):
        
        if(graph2[nx][ny]==0):
          continue
        else:
          
          x = nx
          y = ny
          
          bfs(x,y,graph2)
          sum -= a
          graph2[x][y] = a
          cnt -= 1

  # 새로운영역 check
  
 
   
        
     

for i in range(m):
  for j in range(n):
    cnt = 0
    sum = 0
    graph2 = copy.deepcopy(graph)
    bfs(i,j,graph2)

print(max(s_arr),len(s_arr))