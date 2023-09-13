'''30.Write a Python program to remove spaces from dictionary keys.
Original dictionary: {'S 001': ['Math', 'Science'], 'S002': ['Math','English']}
New dictionary: {'S001': ['Math', 'Science'], 'S002': ['Math',
'English']}'''

d={'S 001': ['Math', 'Science'], 'S 002': ['Math','English']}
l=[]
l2=[]
for x,y in d.items():
    s=''
    l2.append(y)
    for k in x:
        if k==' ':
            pass 
        else:
            s+=k 
    l.append(s)
dic={} 
for i in range(len(l)):
    dic[l[i]]=l2[i] 
print(dic)               


'''s='Hello World'
res=''
for i in s:
    if i==' ':
        pass
    else:
        res+=i
print(res)'''