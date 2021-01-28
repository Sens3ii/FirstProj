import re
text = 'hello world programming techn'
result = re.findall(r'\b\w\w', text)
print(result)
