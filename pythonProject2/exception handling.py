
try:
   a = int(input("enter a number"))
   print (a + 5)
except Exception as e:
    print("some error occurred" , e)