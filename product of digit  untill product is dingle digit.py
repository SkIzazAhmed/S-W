def pro(a):
  a=str(a)
  p=1
  for i in a:
    p=p*int(i)
  return p
x=int(input())
y=[]
j=0
i=x
while i>10:
  y.append(pro(i))
  i=y[j]
  j=j+1
print(len(y))

