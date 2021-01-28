import re
text = '+7-777-7777777 abc +7-771-4567890'
result = re.findall(r'\+7-[1-9]{3}-[0-9]{5}', text)
print(result)

text1 = 'asdf fjdk;afed,fjek,asdf,foo'
result1 = re.split(r'[;, ]', text1)
print(result1)
text2 = 'asdf fjdk;afed,fjek,asdf,foo'
result2 = re.sub(r'[;, ]', ' ', text2)
print(result2)
