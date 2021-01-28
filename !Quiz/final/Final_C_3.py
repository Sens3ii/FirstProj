data_1 = input().split() # data from Barsenal stadium
data_2 = input().split() # data from Arselona stadium

#home stadium of Barsenal
# a and b — goals of the Barsenal and Arselona
a = int(data_1[0]) #B
b = int(data_1[1]) #A

#home stadium of Arselona
# c and d — goals of the Arselona and Barsenal
c = int(data_2[0]) #A
d = int(data_2[1]) #B

if a + d > b + c: # If total goals of Barsenal more
    print('Barsenal')
elif a + d < b + c: # If total goals Arselona more
    print('Arselona')
elif b > d: # If Arselona do more goals, not in home stadium
    print('Arselona')
elif d < b:# If Barsenal do more goals, not in home stadium
    print('Barsenal')
else: # Else - friendship
    print('Friendship')
print(a + d, b + c) # score
