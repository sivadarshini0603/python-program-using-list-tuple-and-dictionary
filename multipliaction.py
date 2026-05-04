print("matrix 1")
r1=int(input("enter the no of rows"))
c1=int(input("enter the no of columns"))
a=[]
print("enter the elements")
for i in range(r1):
   r=[]
   for j in range(c1):
      value=int(input())
      r.append(value)
   a.append(r)
print("matrix 2")
r2=int(input("enter the no of rwos"))
c2=int(input("enter the no of columns"))
if c1!=r2:
   print("matrix mul is failed")
else:
   b=[]
   print("enter the elements")
   for i in range(r2):
      r=[]
      for j in range(c2):
         value=int(input())
         r.append(value)
      b.append(r)
   mul=[]
   for i in range(r1):
      r=[]
      for j in range(c2):
         s=0
         for k in range(c1):
            s=s+a[i][k]*b[k][j]
         r.append(s)
      mul.append(r)
   for i in range(r1):
      for j in range(c2):
         print(mul[i][j],end='\t')
      print()
