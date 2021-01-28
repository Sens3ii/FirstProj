import re
result = re.match('test', 'test prog princ test')
print(result)
print(result.group(0))
print(result.start())
print(result.end())

