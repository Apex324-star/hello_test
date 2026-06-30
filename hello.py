def factorial(n):
   if n==0 or n ==1:
       return 1
    return n*factorial(n-1)
try:    
  nu=int(input("Enter number to be factorized"))
except:
  print("data type should be intiger")
else:   
  print(f"the factorial of {nu} is {factorial(nu)}")
          
