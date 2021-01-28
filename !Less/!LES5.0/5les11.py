import re
text = 'abc tatt eia a bobb'
result = re.findall(r'\b[aeiouAEIOU]\w+', text)
print(result)
text1 = 'abc tatt eia a bobb'
result1 = re.findall(r'\b[^aeiouAEIOU ]\w+', text1)
print(result1)
