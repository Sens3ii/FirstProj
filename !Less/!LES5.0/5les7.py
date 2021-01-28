import re
text = 'test programming technologies testes'
result = re.findall(r'^\w+', text)
print(result)
text1 = 'test programming technologies testes'
result1 = re.findall(r'\w+$', text1)
print(result1)
