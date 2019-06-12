char=input()
char=char.lower()
if(char.isdigit()):
  print("invalid")
elif(char=='!'or char=='@'or char=='#' or char=='$' or char=='%' or char=='^' or char=='&' or char=='*'):
  print("invalid")
elif(char=='a' or char=='e' or char=='i' or char=='o' or char=='u'):
  print("vowel")
else:
  print("consonant")
