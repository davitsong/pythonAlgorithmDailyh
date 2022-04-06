import sys

def move():
  for i in range(n): # 1번부터 n열까지 검사 (idx 0~n-1)
    num = i          # num 시작해서 i 로 끝나는지 확인하기위해 i~n-1까지 모두 확인
    for j in range(h): # 행 이동  ( 0 ~ h-1 인덱스까지 확인)
      if ladder[j][num]: #가로선 이 존대하면
        num +=1 # 열 바꾸어줌
      elif num > 0 and ladder[j][num-1]:#첫번째 열 말고 그 이외의 열 왼쪽에 가로선있으면
        num -=1 #  열 왼쪽으로 이동
    if num != i: return False # i 랑 num 다르면 False return

  return True # 모든열이 시작과 끝이 같을 경우 return True

def dfs(cnt,x,y):  # cnt -> 현재 놓은 가로선의 개수, (x,y) -> 진행되고 있는 좌표
  
  global  ans  # 필요한 최소 개수 출력하기 위해  ans 전역변수로 사용 
  
  if move():              # 출발점이 도착점 모든 열이 일치할 경우 
    ans = min(ans,cnt)    # ans 값을 갱신되는 ans와 만족하는 가로선 개수 비교하여 최소값 으로 설정
    return # 종료
    
  elif cnt==3 or ans<=cnt : # 도착점이 정상이지 않을때 cnt가 3일경우 다음 호출에서 cnt3이 넘어가고, 현재 갱신된 최소의 ans보다 작으면 더 이상 필요 없으므로 종료
    return

  
  for i in range(x,h): # 행 탐색 (x: 0 ~ h-1)
    
    if i == x: k = y # 행이 교체되지 않았을 경우 진행되고 있는 열부터 확인 진행

    else: k = 0 # 행바뀌면 첫째 열부터 시행
      
    for j in range(k, n-1): # 열 별 탐색 (j -> k ~ n-1)
      if not ladder[i][j] and not ladder[i][j+1]:
        # 가로선이 현재위치와 오른쪽에 존재하지 않는 경우
        if j > 0 and ladder[i][j-1]: continue
        # 첫째 열이 아닌경우 현재위치 왼쪽에 가로선이 존재하는 경우 -> 다음 열 탐색
        ladder[i][j] = 1 # 현재 좌표에 가로선 넣음
        dfs(cnt+1, i, j + 2 ) #가로선 개수 증가 시키고  바로옆에 있으면 안되므로 j+2 부터 다시 탐색
        ladder[i][j] = 0 #재귀 풀릴때 가로선 없애기
    


# print(n,h,m)  세로선 개수 n행 가로선 개수 h열 n*h 가로 막대기 개수 m 개   h*n 행렬

input = sys.stdin.readline

ans = 4 #정답 4로 초기화

n,m,h = map(int,input().split())

ladder = [[0]*n for _ in range(h)]

if (m==0):
  print(0)
  exit(0)
else:
  
  for _ in range(m):  # 처음 정해진 가로선 이차원 배열에 입력
    a,b=map(int,input().split())
    ladder[a-1][b-1]=1 

dfs(0,0,0)  #브루트포스 시작

if ans<=3:
  print(ans)
else:
  print(-1)








  
  