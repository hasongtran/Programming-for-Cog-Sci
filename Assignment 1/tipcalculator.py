tipRate = float(input('What tip rate do you want to use? [.05 to .25] '))
if .05 <= tipRate < .25:
    price = float(input('Enter the price of the meal: '))
    tipPrice = float(tipRate * price)
    totalPrice = float(tipPrice + price)
    print('The tip for your meal is $', tipPrice, 'and the total price is $', totalPrice)

else:
    print('Next time, enter a more reasonable tip rate')
