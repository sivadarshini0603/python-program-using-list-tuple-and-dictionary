d={}
s=input("enter a sentence:").split()
d["beach"]="park"
d["mom"]="friend"
for i in s:
   if i in d:
      print(d[i],end="")
   else:
      print(i,end="")
