import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)
print("The first white-space character is located in position:", x.start())