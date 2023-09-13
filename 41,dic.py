'''41.Write a Python program to filter the height and width of students, which are stored in a
dictionary.
Original Dictionary:
{'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8,
66)}
Height > 6ft and Weight> 70kg:
{'Cierra Vega': (6.2, 70)}  '''

d={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8,66)}
dic={}
for i in d:
    for j in d[i]:
        if type(j)==int:
            w=j 
        else:
            h=j 
    if  w>=70 and h>=6:
        dic[i]=d[i] 
print(dic)                   