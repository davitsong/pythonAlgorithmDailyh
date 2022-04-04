import sys
from itertools import combinations as com   #조합사용

input = sys.stdin.readline

n = int(input())

arr1 = [] # 입력받은 list
arr2 = []  # combination 돌릴 set
k = set()  # combination 돌릴 set
ans =  []  # 전체 합 차 list 

for i in range(n):
  arr1.append(list(map(int,input().split()))) # 이차원 배열에 입력받음
  arr2.append(i)         # combination 돌 릴 list에 입력받음
  k.add(i)               # index set에 입력받음


res = list(com((arr2),n//2))    # 반을 나눈 조합 list에 넣음 

for i in res: # 모든 스타트 경우
  a = set(i) #스타트 set
  b = k - a  #링크 set
  #print(a,b)
  c = list(a) #스타트 list
  d = list(b) #링크 list
  #print(c,d)
  res1 = list(com(c,2))  # 반을 나눈 조합 2개씩으로 나눔
  res2 = list(com(d,2))  # 반을 나눈 조합 2개씩으로 나눔
  sum1 = 0
  sum2 = 0
  #print(res1,res2)
  for j in res1:         # 스타트 전체 합
    sum1+=arr1[j[0]][j[1]]+arr1[j[1]][j[0]]
  for j in res2:         # 링크 전체 합 
    sum2+=arr1[j[0]][j[1]]+arr1[j[1]][j[0]]
  ans.append(abs(sum1-sum2))  # 스타트 링크 차이 ans 리스트에 append
  
print(min(ans))

  




