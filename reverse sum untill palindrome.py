def is_palinderome(a):
  if a==a[::-1]:
    return True
  else:
    return False
x=input()
i=x
count=0
while True:
  if(is_palinderome(i)):
    print(count)
    break
  else:
    i=str(int(i)+int(i[::-1]))
    count+=1