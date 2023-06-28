dic={"num":23,"sel":40,"tuple":(20,3,12,11),"list":[1,3,5,0,2]}
print(dic["sel"]+dic['num']) 

"""dil={"a":{1:'hello',2:'hii',3:'navgurukul'},'b':{4:'wel',5:'come'}}
dil['b'][6]="to" 
print(dil["b"])

dir={'nil':1.9,'bil':2}  
dir['mil']=3 
print(dir) """

'''class nav:
    var_streght=100
    def resi():
        print("called res function")
    resi()  '''


d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
for i in d1:
    if i is not d2:
        d2[i]=d1[i]
print(d2)    

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)