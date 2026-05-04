list=[]
n=int(input("enter number of elements"))
for i in range(n):
   list.append(int(input("enter elements")))
while True:
   print("1.insert at position")
   print("2.append elements")
   print("3.compare lists")
   print("4.print id of elements")
   print("5.find first occurance")
   print("6.exit")
   ch=int(input("enter choice"))
   if ch==1:
      pos=int(input("enter position"))
      val=int(input("enter value:"))
      list.append(val)
      list=list[:pos]+[val]+list[pos:-1]
      print("updated list..",list)
   elif ch==2:
      val=int(input("enter value:"))
      list.append(val)
      print("updated list",list)
   elif ch==3:
      list2=[]
      n2=int(input("enter no of elements"))
      for i in range(n2):
         x=int(input("enter elements"))
         list2.append(x)
      if list==list2:
         print("lists are equal")
      else:
         print("lists are not equal")
   elif ch==4:
      for i in list:
         print("elements:",i,"ID",id(i))
   elif ch==5:
      item=int(input("enter item"))
      if item in list:
         print("1st occurences at index",list.index(item))
      else:
         print("item not exist")
   elif ch==6:
      break
   else:
      print("invalid choice")
