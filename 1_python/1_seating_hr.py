#hackerEarth SeatingProblem
t = int(input(''))
seats = []
for u in range(0,t):
    n = int(input(''))
    if n > 108:
        exit()
    seats.append(n)

valSe = 0
i = 0

for a in seats:
    valSe = a - 12*(int(a/12))

    if valSe == 1:
        print(a + 11, 'WS')
    elif valSe == 2:
        print(a + 9, 'MS')
    elif valSe == 3:
        print(a + 7, 'AS')
    elif valSe == 4:
        print(a + 5, 'AS')
    elif valSe == 5:
        print(a + 3, 'MS')
    elif valSe == 6:
        print(a + 1, 'WS')
    elif valSe == 7:
        print(a - 1, 'WS')
    elif valSe == 8:
        print(a - 3, 'MS')
    elif valSe == 9:
        print(a - 5, 'AS')
    elif valSe == 10:
        print(a - 7, 'AS')
    elif valSe == 11:
        print(a - 9, 'MS')
    elif valSe == 12:
        print(a - 1, 'WS')
    elif valSe == 0:
        print(a - 11, 'WS')
    