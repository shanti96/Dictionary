'''Q8.Write a Python program to check whether a given key already exists in a dictionary.'''

d={'name':'spya','vill':'P.R.C.G','gen':'female'}
key=input('enter the key = ')
for i in d:
    if key==i:
        print('key already exists in a dictionary')
        break
else:
    print('not exists') 
