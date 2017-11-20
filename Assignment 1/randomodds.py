counter = 1
while counter <= 20:
    import random
    newRandom = random.randint(1,100)
    if newRandom % 2:
        print(newRandom)
        counter = counter + 1