import sys

data = []
n = int(input())
ans = [0]*(n+1) #i번째 이후 최대값 역으로접근

for i in range(n):
  data.append(list(map(int,sys.stdin.readline().split())))

#print(data)
#print(ans)

for i in range(n-1,-1,-1):
  if i + (data[i][0])> n:
    ans[i] = ans[i+1]
  else:
    ans[i] = max(data[i][1] + ans[i+data[i][0]],ans[i+1])


#print(ans)
#print(ans[0])
