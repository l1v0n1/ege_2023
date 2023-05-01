print('x y z w')
for x in range(0,2):
    for y in range(0,2):
        for w in range(0,2):
            for z in range(0,2):
                F = (x == (w or y)) or ((not(w) or z) and (not(y) or w))
                if F:
                    print(x,y,z,w)

    
    

