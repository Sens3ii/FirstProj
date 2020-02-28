# 1
a = -11
print(abs(a))
# 2
l = [True, True, True]
x = all(l)
print(x)  # if some false or 0 it'll be false
elem1 = {'title': 'abc', 'description': 'test', 'id': 'page', 'data': 'test1'}
elem2 = {'title': 'abc2', 'description': 'test2',
         'id': 'page2', 'data': 'test2'}
elem3 = {'title': 'abc3', 'description': 'test3'}
keys = ['title', 'description', 'id', 'data']
data = [elem1, elem2]
data1 = [elem1, elem2, elem3]
for d in data1:
    for key in keys:
        if key not in d.keys():
            print("Error1")
for d in data1:
    if not all([key in d.keys() for key in keys]):
        print("Error2")
