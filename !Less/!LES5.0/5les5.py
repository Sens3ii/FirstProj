import re
result = re.findall('.', 'programming technologis')
print(result)
result2 = re.findall('.i', 'programming technologis')
print(result2)
result3 = re.findall('m+', 'programming technologis mmmaatharfakkerr')
print(result3)
result4 = re.findall(
    '\w+', 'programming technologis mmmussskkoooorrttaaa AAAABBBCCC')
print(result4)
result5 = re.findall(
    '\W+', 'programming technologis mmmussskkoooorrttaaa AAAABBBCCC 123abc dsd123 123')
print(result5)
result6 = re.findall(
    '\d+', 'programming technologis mmmussskkoooorrttaaa AAAABBBCCC 123abc dsd123 123')
print(result6)
result6 = re.findall(
    '\D+', 'programming technologis mmmussskkoooorrttaaa AAAABBBCCC 123abc dsd123 123')
print(result6)
