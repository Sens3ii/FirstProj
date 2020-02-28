from collections import Counter
print(Counter('aabbcc'))
if Counter('abcabc') == Counter('aabbcc'):
    print("Yes")
else:
    print("No")