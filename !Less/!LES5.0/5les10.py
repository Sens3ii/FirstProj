import re
text = 'AAA 34-3456 12-01-2020, exam 23-04-2020'
result = re.findall(r'\d\d-\d\d-\d\d\d\d', text)
print(result)
text1 = 'AAA 34-3456 12-01-2020, exam 23-04-98'
result1 = re.findall(r'\d{2}-\d{2}-\d{2,4}', text1)
print(result1)
text2 = 'AAA 34-3456 12-01-2020, exam 23-04-98'
result2 = re.findall(r'(\d{2})-(\d{2})-(\d{2,4})', text2)
print(result2)
