import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)
result = re.findall("^The.*Spain$", txt)
result2 = re.findall("^Thee.*Spain$", txt)
print(result)
print(result2)