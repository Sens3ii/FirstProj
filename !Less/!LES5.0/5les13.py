import re
text = '12 asdf23 asdf34asdf'
result = re.finditer('d+', text)
for r in result:
    print(r.start(),r.end())
