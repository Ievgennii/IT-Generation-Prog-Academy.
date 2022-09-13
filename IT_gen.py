print("Buying bitcoins with dollars.")
print("Enter 'q' to quit.")
while True:
    bitcoin_price = input("\nWhat is Bitcoin price today?: ")
    if bitcoin_price == 'q':
        break
    number_dollars = input("How much $ do you have?: ")
    if number_dollars == 'q':
        break
    try:
        answer = float(number_dollars) / float(bitcoin_price)
    except ValueError:
        print('You can only enter numbers')
    except ZeroDivisionError:
        print("Price cannot be equal to 0")
    else:
        print(f'You can buy {round(answer, 7)}')
