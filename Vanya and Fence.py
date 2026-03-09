n,h=map(int,input().split())
k=list(map(int, input().split()))
for i in range(len(k)):
  if k[i]>h:
    k[i]=2
  else:
    k[i]=1
print(sum(k))
