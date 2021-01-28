allMoney = input().split()
azMoney = int(allMoney[0])
daurMoney = int(allMoney[1])
for i in range(100):
    if azMoney > daurMoney:
        print(i)
        break
    azMoney = azMoney*3
    daurMoney = daurMoney*2
