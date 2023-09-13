'''Q13.Write a Python program to sum all the items in a dictionary.'''

dic={1:12,2:32,3:8}

s=0
for i in dic:
    s+=dic[i]
print('sum=',s)

'''Q14.Write a Python program to multiply all the items in a dictionary'''

m=1
for j in dic:
    m=m*dic[j]
print('multiply = ',m)  

'''Q15.Write a Python program to remove a key from a dictionary.'''

d={'a':1,'c':9,'r':3,'s':5}
print(d.pop('r'))
print(d) 


'''Q16.Write a Python program to map two lists into a dictionary.'''

l1=['a','b','c']
l2=[2,9,3]
d1={}
for i in range(len(l1)):
    d1.update({l1[i]:l2[i]})
print(d1) 

'''Q17.Write a Python program to sort a dictionary by key.'''

dic1={'a':1,'c':8,'b':5,'e':2}
di=sorted(dic1)
print(di)

'''Q18.Write a Python program to get the maximum and minimum value in a dictionary.'''

dic1={'a':1,'c':8,'b':5,'e':2}
d3=dic1.values()
m=0
min=1
for i in dic1:
    if dic1[i]<=min:
        min=dic1[i]
    elif m<dic1[i]:
        m=dic1[i] 
print('max=',m, 'min=',min)         