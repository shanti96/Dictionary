'''31.. Write a Python program to get the top three items in a shop. Go to
the editor
Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55,
'item5': 24}
Expected Output:
item4 55
item1 45.5
item3 41.3 '''
n=0
l=[]
d={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55,'item5': 24}
for i in range(3):
    v=0
    for x,y in d.items():
        if v<y and i<1:
            a=y
            v=a
            k=x 
        elif v<a and i<2:
            b=y
            v=b
            k=x
        elif v<b and i<3:
            c=y 
            v=c
            k=x         
    l.append([k,v]) 
print(l)           
            