myList = [2,8,10,23,12,4]

i=0 , j= len(myList)-1
while (i < j):
  aux = myList[j]
  myList[j]= aux
  print(f"Final list :{myList}" )
