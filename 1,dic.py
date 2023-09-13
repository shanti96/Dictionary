'''Q1.Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})'''


d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
dic={}
for i in d1:
    for j in d2:
        if i==j:
            s=d1.get(i)+d2.get(j)
            d1[i]=s
le=[d1,d2] 
for k in le:
    for x,y in k.items():
        if x not in dic:
            dic[x]=y 
print(dic)            
