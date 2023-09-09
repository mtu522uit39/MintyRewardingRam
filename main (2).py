print("checking leap year")
year=int(input("enter the year:"))
if(year%4 == 0 and year%100!=0) or (year%400 == 0):
  print (year ,"is not a leap year.")
else:
  print(year,"is not a leap year.")
  print("factorial")
  num =5
  factorial =1 
  if num<0:
    print("factorial does not exists")
  elif num==0:
    print ("the factorial of 0 is 1")
  else:
    for i in range(1,num+1):
      factorial=factorial*i
      print("the factorial of",num,"is",factorial)
  