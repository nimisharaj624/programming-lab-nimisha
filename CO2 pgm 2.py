nterms = int(input("Enter a terms "))

x=0
y=1
count = 0

if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(x)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(x)
       nth = x + y
       x = y
       y = nth
       count += 1