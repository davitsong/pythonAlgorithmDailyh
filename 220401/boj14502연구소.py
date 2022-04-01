import sys
from collections import deque
import copy
from itertools import combinations as com

input = sys.stdin.readline


graph_o = []

n,m =  map(int,input().split())
for _ in range(n):
  graph_o.append(list(map(int,input().split())))
             

# 상 우 하 좌
dx = [-1,0,1,0]
dy = [0,1,0,-1]

survive = 0


wall = []
virus = []

for i in range(n):
  for j in range(m):
    if(graph_o[i][j]==2):
      virus.append((i,j))    #virus의 좌표 list추가
    if(graph_o[i][j]==0):
      wall.append((i,j))     #벽이 가능한 좌표 list추가

def bfs(walls):
  
  graph = copy.deepcopy(graph_o)
  deq = deque(virus)         # virus list deque에 삽입
  safe = 0
  
  for a, b in walls:      #벽세우기
    graph[a][b] = 1
    #print(a,b)

  while deq:              #가능한 바이러스 퍼트리기
    x,y = deq.popleft()
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      if (0 <= nx < n and 0 <= ny <m):
        if(graph[nx][ny]==0):
          graph[nx][ny] = 2
          deq.append((nx,ny))

  for i in range(n):       #safe 개수 check 하고 return
    for j in range(m):
      if(graph[i][j]==0):
        safe += 1
  #print(safe)      

  return safe
      


for i in com(wall,3):
  survive = max(survive, bfs(list(i)))
  
print(survive)
    
  