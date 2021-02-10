x=str(input("Enter data:"))
for i in range(0,len(x)):
    if i==0:
        print(x[i])
    else:
        if x[i] == x[0]:
            print("$")
        else:
            print(x[i])

