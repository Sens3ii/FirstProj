#ONLY NAMES OF PRODUCT

import re
pattern = r'.*\.\n{1}[^,#№%0-9]+'

f = open('raw.txt', 'r', encoding='utf-8')
text = f.read()

result = re.findall(pattern, text)
for it in result:
    print(it)
