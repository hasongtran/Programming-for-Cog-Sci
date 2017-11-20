triangle = input('Is your triangle a right triangle? yes/no ')
if triangle == 'yes' or triangle == 'no':
    if triangle == 'no':
        print("This code can't help you")
    else:
        sideA = int(input('What is the length of side A? '))
        sideB = int(input('What is the length of side B? '))
        sideC = int(sideA * sideA + sideB * sideB)
        import math
        c_unsquared = math.sqrt(sideC)
        print('The length of the third side is ', c_unsquared)
else:
    print("I don't understand")
