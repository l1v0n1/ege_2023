for a in range(300, 1, -1): 
    k = 0
    for x in range(0, 300):
        for y in range(0, 300):
            if ((x <= 9) <= (x * x <= a)) and ((y*y <= a) <= (y <= 9)):
                k += 1
    if k == 90_000:
        print(a)
        break