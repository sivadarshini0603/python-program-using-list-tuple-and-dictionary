tel={}
n=int(input("enter no of contacts"))
for i in range(n):
   name=input("enter name")
   num=int(input("enter phn no"))
   tel[name]=num
   print("telephone directory")
for i in tel:
   print(i,":",tel[i])
