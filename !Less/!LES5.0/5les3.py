import re
result = re.split(',', '1,2,3,4,5')
print(result)
result1 = re.split('TTT', 'AAATTTBBBTTTCCC')
print(result1)
result2 = re.split('TTT', 'AAATTTBBBTTTCCC', 1)
print(result2)
result3 = re.sub(',', ' ', "1,2,3,4,5")
print(result3)
