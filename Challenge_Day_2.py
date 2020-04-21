n=int(input("Enter the year:: "))
def fun1(n):
  if(n>2011):
    while(n>=2011):
      n=n-12
    return n
  elif(n<2000):
    while(n<=2000):
      n=n+12
    return n
  else:
    return n
n=fun1(n)
if(n==2000):
  print("Dragon")
elif(n==2001):
  print("Snake")
elif(n==2002):
  print("Horse")
elif(n==2003):
  print("Sheep")
elif(n==2004):
  print("Monkey")
elif(n==2005):
  print("Rooster")
elif(n==2006):
  print("Dog")
elif(n==2007):
  print("Pig")
elif(n==2008):
  print("Rat")
elif(n==2009):
  print("Ox")
elif(n==2010):
  print("Tiger")
elif(n==2011):
  print("Hare")