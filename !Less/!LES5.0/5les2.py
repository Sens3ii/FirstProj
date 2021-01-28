import re
result = re.search('programming', 'test programming')
print(result.group())
print(result.start())
print(result.end())
