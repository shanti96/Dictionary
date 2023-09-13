'''38.. Write a Python program to drop empty Items from a given Dictionary.
Original Dictionary:
{'c1': 'Red', 'c2': 'Green', 'c3': None}
New Dictionary after dropping empty items:
{'c1': 'Red', 'c2': 'Green'} '''


d={'c1': 'Red', 'c2': 'Green', 'c3':None }
dic={}
for x,y in d.items():
    t=type(y)
    print(t) 
    if t == type(None):
        pass 
    else:
        dic[x]=y 
print(dic)         
