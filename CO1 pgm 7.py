lst=[1,2,3,4,5,6,7,8]
lst1=[2,1,3,5,7,10,6,9]
p=int(0)
q=int(0)
for i in lst and lst1:
    if len(lst)==len(lst1):
        print("Lists are same length")
        break
    else:
        print("Lists have different length")
        break
for i in range(0,len(lst) and len(lst1)):
    p=p+lst[i]
    q=q+lst1[i]
for i in range(0, len(lst) and len(lst1)):
    if p==q:
        print("Sum of values are same")
        break
    else:
        print("Sum of values are different")
        break
print("Elements that matched are:")
l=[]
for i in range(0,len(lst)):
    for j in range(0,len(lst1)):
        if lst[i]==lst1[j]:
            l.append(lst[i] and lst1[j])
        else:
            x=i
            continue
print(l)
