dic={'name':'spd','vill':'p.r.c.g',}
dic['city']='khowai'
print(dic)


#Q1.Write a Python program to combine two dictionary adding values for common keys.
#d1 = {'a': 100, 'b': 200, 'c':300}
#d2 = {'a': 300, 'b': 200, 'd':400}
#Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'b': 300, 'a': 200, 'd':400}
for i in d1:
    if i in d2:
        d2[i]=d1[i]+d2[i]
    else:
        d2[i]=d1[i]
print(d2)
