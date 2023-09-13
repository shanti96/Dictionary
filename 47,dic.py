'''47.A Python Dictionary contains List as value. Write a Python program to clear the list values in
the said dictionary.
Original Dictionary:
{'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
Clear the list values in the said dictionary:
{'C1': [], 'C2': [], 'C3': []} '''

'''d={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
for x,y in d.items():
    y.clear()
    d[x]=y
print(d)   ''' 




'''48.Write a Python program to find the length of a given dictionary values.
Original Dictionary:
{1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
Length of dictionary values:
{'red': 3, 'green': 5, 'black': 5, 'white': 5}
Original Dictionary:{'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
Length of dictionary values:
{'Austin Little': 13, 'Natasha Howard': 14, 'Alfred Mullins': 14, 'Jamie Rowe': 10} '''

'''d={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
d1={}
for i in d.values():
    l=len(i)
    d1[i]=l 
print(d1) '''


'''49.Python: Access dictionary key's element by index
num = {'physics': 80, 'math': 90, 'chemistry': 86}
physics
math
chemistry '''

'''n={'physics': 80, 'math': 90, 'chemistry': 86}
for i in n:
    print(i)'''


'''Q50.Write a Python program to convert a given dictionary into a list of lists.
Original Dictionary:
{1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
Convert the said dictionary into a list of lists:
[[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]
Original Dictionary:
{'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
Convert the said dictionary into a list of lists:
[['1', 'Austin Little'], ['2', 'Natasha Howard'], ['3', 'Alfred Mullins'], ['4', 'Jamie Rowe']] '''

d={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
l=[]
for x,y in d.items():
    l.append([x,y])
print(l)     
