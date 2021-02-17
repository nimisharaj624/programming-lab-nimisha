def rec_fact(i):
  if i==1:
   return 1
  else:
    return(i * rec_fact(i-1))
n=int(input("Enter a number : "))
if n>= 1:
 print("The factorial of the number is ",rec_fact(n))
