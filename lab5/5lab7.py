import re

txt = "hello world"

#Check if the string ends with 'world':

x = re.findall("world$", txt)
print(x)
if (x):
  print("Yes, the string ends with 'world'")
else:
  print("No match")