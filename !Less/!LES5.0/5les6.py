import re
text = '123 abc12kk 24 45lll4'
result = re.findall(r'\b\d+\b', text)
print(result)
text1 = 'abda9cb'
result1 = re.findall(r'[a9c].', text1)
print(result1)
text2 = '1a abc 2bc ttt3d daf5.'
result2 = re.findall(r'[1-8]\w', text2)
print(result2)
text3 = '1a abc 2bc ttt3d daf5.'
result3 = re.findall(r'[^1-8]\w', text3)
print(result3)
text4 = 'aaa kkaall lalaaaal abafa'
result4 = re.findall(r'a{2,}', text4)
print(result4)
text5 = 'aaa kkaall lalaaaal abafa'
result5 = re.findall(r'\w+', text5)
print(result5)
