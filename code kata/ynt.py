a1,b1=map(int,input().split())
if(a1<b1):
  for i in range(a1+1,b1,1):
     if i%2==0:
        print(i,end=' ')
