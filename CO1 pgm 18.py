def Merge(dict1, dict2):
    return(dict2.update(dict1))
dict1 = {'x': 10, 'y': 8}
dict2 = {'a': 6, 'b': 4}
print(Merge(dict1, dict2))
print(dict2)