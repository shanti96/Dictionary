'''36.Write a Python program to match key values in two dictionaries.
Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
Expected output: key1: 1 is present in both x and y '''

d1={'key1': 1, 'key2': 3, 'key3': 2}
d2={'key1': 1, 'key2': 2}
for x,y in d1.items():
    for i,j in d2.items():
        if x==i and y==j:
            print(x,':',y,'is present in both d1 and d2')
            