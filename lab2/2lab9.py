def isMutubleIn(mytuple):
    for i in mytuple:
        if type(i) == dict or type(i) == list or type(i) == set:
            return True
    return False


print(isMutubleIn((10, 2, 5, [4, 8, 2], 3, 5)))
print(isMutubleIn((5, 2.5, 8, 4, 'Hi', -5, True, 6)))
