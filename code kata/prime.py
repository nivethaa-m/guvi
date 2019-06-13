val=int(input())
if val>1:
  for i in range(2,val):
    if val%i == 0:
      print ("no")
      break
  else:
    print ("yes")
else:
  print ("no")
