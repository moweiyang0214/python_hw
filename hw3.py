while True:
  try:
    count = int(input('Enter count:'))
    price = float(input('enter price for each one:'))
    pay = count * price
    print('the price is: ',pay)
    break
  except ValueError:
    print('Error, please enter numeric one.:)')