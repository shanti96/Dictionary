'''44.Write a Python program to split a given dictionary of lists into list of dictionaries.
Original dictionary of lists:
{'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
Split said dictionary of lists into list of dictionaries:[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78},
 {'Science': 62, 'Language':84}, {'Science': 95, 'Language': 80}]'''

d={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]} 
k=list(d)
le=list(d.values()) 
l=[] 
for i in range(len(le[0])):
    d1={}
    for j in range(len(k)):
        d1[k[j]]=le[j][i] 
    l.append(d1)
print(l)         