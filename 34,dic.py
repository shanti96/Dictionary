'''38.. Write a Python program to drop empty Items from a given Dictionary.
Original Dictionary:
{'c1': 'Red', 'c2': 'Green', 'c3': None}
New Dictionary after dropping empty items:
{'c1': 'Red', 'c2': 'Green'} '''

d={'c1': 'Red', 'c2': 'Green', 'c3':None}
d1={}
for x,y in d.items():
    if y is not None:
        d1.update({x:y}) 
print(d1)     