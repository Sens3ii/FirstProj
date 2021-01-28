import re
pattern = r'(Порядковый номер чека)(.*)'
f = open('raw.txt', 'r', encoding='utf-8')
text = f.read()
result = re.findall(pattern, text)
print(result)
