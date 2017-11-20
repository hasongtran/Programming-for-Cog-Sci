loop = 1
while loop:
    tipRate = float(input('What tip rate do you want to use? [.05 to .20] '))
    if .05 <= tipRate < .20:
        price = float(input('Enter the price of the meal: '))
        tipPrice = float(tipRate * price)
        totalPrice = float(tipPrice + price)
        print('The tip for your meal is $', tipPrice, 'and the total price is $', totalPrice)
        loop = 0
    else:
        print('Error: tip rate must be between .05 and .20')
    if tipRate == "":
        print('Got a null input')


