import re
pattern = re.compile('test')
result = pattern.findall('hi test hi test')
print(result)
