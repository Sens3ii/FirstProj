s = str(input())
a = int(s.find('f'))
b = int(s.rfind('f'))
if a!=-1 and b!=-1 and b!=a:
    print(a,b)
elif a==b and a!=-1:
    print(a)


