'''36.Write a Python program to match key values in two dictionaries.
Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
Expected output: key1: 1 is present in both x and y '''

x={'key1': 1, 'key2': 3, 'key3': 2}
y={'key1': 1, 'key2': 2} 
d={}
for a,b in x.items():
    for p,k in y.items():
        if a==p and b==k :
            d[a]=b 
print(d)            