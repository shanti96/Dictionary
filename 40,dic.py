'''40. Write a Python program to convert more than one list to nested dictionary.
Original strings:
['S001', 'S002', 'S003', 'S004']
['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
[85, 98, 89, 92]
Nested dictionary:
[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}},
{'S004': {'Saim Richards': 92}}] '''

a=['S001', 'S002', 'S003', 'S004']
b=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
c=[85, 98, 89, 92] 
dic={}
for i in range(4):
    d1={}
    d1[b[i]]=c[i]
    dic[a[i]]=d1
print(dic)    
