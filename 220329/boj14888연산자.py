import sys

n = int(input())

arr1  = list(map(int,sys.stdin.readline().split()))

add, sub, mul, div = map(int,sys.stdin.readline().split())

#print(n,arr1,add,sub,mul,div)

maxsize = -1e9
minsize = 1e9

# 10**9 10**-9 안되는 이유?



def dfs(curr,idx,add,sub,mul,div):
    global maxsize
    global minsize
    print(maxsize,minsize)
    if(idx==n):
      #print(curr)
      maxsize=max(maxsize,curr)
      minsize=min(minsize,curr)
      #print(maxsize,minsize)
      return
      
    if add>0:
      dfs(curr+arr1[idx],idx+1,add-1,sub,mul,div)
    if sub>0:
      dfs(curr-arr1[idx],idx+1,add,sub-1,mul,div)
    if mul>0:
      dfs(curr*arr1[idx],idx+1,add,sub,mul-1,div)
    if div>0:
      dfs(int(curr/arr1[idx]),idx+1,add,sub,mul,div-1) #C++14 음수나눗셈과 python 음수 나눗셈 차이점?
      
dfs(arr1[0],1,add,sub,mul,div)
print(maxsize)
print(minsize)

