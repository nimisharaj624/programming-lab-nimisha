n=int(input("Enter the numbers:"))
for x in range(n):
    for y in range(x):
        print ('* ', end="")
    print('')

for x in range(n,0,-1):
    for y in range(x):
        print('* ', end="")
    print('')