import re
pattern = r'(.*)\n{1}(.*)\n{1}(.*)\n{1}(Stoimost)\n{1}(.*)'
f = open('raw.txt', 'r')
text = f.read()
result = re.findall(pattern, text)
print(result)
