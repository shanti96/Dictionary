'''51.Write a Python program to filter even numbers from a given dictionary values.
Original Dictionary:
{'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
Filter even numbers from said dictionary values:
{'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
Original Dictionary:
{'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
Filter even numbers from said dictionary values:
{'V': [], 'VI': [], 'VII': [2]} '''

'''d={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
a=list(d)
d1={}
l=list(d.values())
for i in range(len(a)):
    l1=[] 
    for j in range(len(l[i])):
        if l[i][j]%2==0:
            l1.append(l[i][j])  
    d1[a[i]]=l1 
print(d1)    '''


'''52. Write a Python program to find the specified number of maximum values in a given
dictionary.
Original Dictionary:
{'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
1 maximum value(s) in the said dictionary:
['f']
2 maximum value(s) in the said dictionary:
['f', 'i']
5 maximum value(s) in the said dictionary:
['f', 'i', 'g', 'd', 'c'] '''

s={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
m=0
l=[]
for x,y in s.items(): 
    if m<y:
        m=y 
        k=x
l.append(k) 
print(l)    

