emp=[]
no=int(input("Enter no of employee"))
for i in range (no):
   print("Enter employee details",i+1)
   e_id=int(input("Enter employee id"))
   n=input("Enter employee name")
   s=int (input("Enter salary"))
   e=(e_id,n,s)
   emp.append(e)
print("Employee details")
for e in emp:
   print(e)
s_id=int(input("\n Enter employee ID to search"))
found=False
for e in emp:
   if e[0]==s_id:
      print("Employee found",e)
      found=True
if not found:
   print("Employee not found")
high=emp[0]
for e in emp:
   if e[2]>high[2]:
      high=e
print("\n Enployee with highest salary:",high)
print("\n Employee with salary of above 50000")
for e in emp:
   if e[2]>50000:
      print(e)
