for i in range(1, 999):
    n = bin(i)[2:]
    if int(n) % 2 == 0:
        n = str(n)
        n = f'1{n}0'
    else:
        n = str(n)
        n = f'11{n}11'

    finish = int(n, base=2)
    if finish >= 52:
        print(finish)
        break
        