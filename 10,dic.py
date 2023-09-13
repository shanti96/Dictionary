'''Q11.Write a Python script to merge two Python dictionaries'''

d1={'name':'spya','vill':'P.R.C.G','gen':'female'}
d2={'hight':165,'state':'tripura'}
for x,y in d2.items():
    d1[x]=y
print(d1)    