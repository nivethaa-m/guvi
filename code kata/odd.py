ax,bx=map(int,input().split())
if(ax<bx):
  for i in range(ax+1,bx,1):
     if i%2!=0:
        print(i,end=' ')
