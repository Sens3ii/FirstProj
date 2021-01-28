def get_sum(path):  
    file = open("2.txt")
    file.seek(0)
    s = file.readline()
    l = s.split()
    return l

list = get_sum("2.txt")
print(list)
def get_str_sum(s):
    list = s.split()
    sum = 0
    for l in list:
        sum += int(l)
    return sum
with open("1.txt") as file:
    for line in file:
        print(get_str_sum(line), end = ' ')