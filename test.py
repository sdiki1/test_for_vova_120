x = 0
y = 0

while True:
    x += 1
    y += 1
    if x is y:
        print(f"{id(x)}, {id(y)} {x}: equal!")
    else:
        print(f"{id(x)}, {id(y)} {x}: Not equal!")
        break
