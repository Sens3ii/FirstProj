import re

txt = "hello world"

#Check if the string starts with 'hello':
x = re.findall("^hello", txt)
print(x)
if (x):
  print("Yes, the string starts with 'hello'")
else:
  print("No match")