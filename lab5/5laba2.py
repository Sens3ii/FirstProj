# ONLY COST
import re
pattern = r'Стоимость\n{1}.*'

f = open('raw.txt', 'r', encoding='utf-8')
text = f.read()

result = re.findall(pattern, text)
i = 1
for it in result:

    print(str(i)+': ' + str(it))
    i += 1
