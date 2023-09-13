'''33.Python: Print a dictionary line by line
students = {'Aex':{'class':'V',
'rolld_id':2},
'Puja':{'class':'V',
'roll_id':3}}
Sample Output:
Aex
class : V
rolld_id : 2
Puja
class : V
roll_id : 3'''

d={'Aex':{'class':'V','rolld_id':2},'Puja':{'class':'V','roll_id':3}}
for x,y in d.items():
    print(x)
    for i,j in y.items():
        print(i,':',j)