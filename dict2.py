m={}
n=int(input("enter no of records"))
for i in range(n):
   num=(input("enter mobile num:"))
   name=input("enter name")
   m[num]=name
search=input("enter num to search")
if search in m:
   print("name:",m[search])
else:
   print("num not found")
