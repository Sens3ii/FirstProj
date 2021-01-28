import re
nameOfFile = 'datausers.txt'
myfile = open(nameOfFile, 'r')
datas = myfile.read()
textLookFor = r"Name:(.*)"
results = re.findall(textLookFor, datas)
print(results)
