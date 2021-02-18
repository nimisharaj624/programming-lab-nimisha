print("Enter the number: ")
n = input()

n = int(n)
print("\nFactors of", n)

i = 1
while i<=n:
    if n%i==0:
        print(i)
    i = i+1