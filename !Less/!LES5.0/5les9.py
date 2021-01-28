import re
text = 'abc.test@gmail.com xyz@mail.ru'
result = re.findall(r'@\w+.\w+', text)
print(result)
import re
text1 = 'abc.test@gmail.com xyz@mail.ru'
result1 = re.findall(r'@(\w+.\w+)', text1)
print(result1)

