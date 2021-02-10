def change(string):
      return string[-1:] + string[1:-1] + string[:1]
string=input("Enter string:")
print(change(string))