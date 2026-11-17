
units = float(input('Enter units input: '))

match units:
    case units if units < 100:
        billamount = units * 3.00

    case units if units < 200:
        billamount = 100 * 3.00 + (units - 100) * 3.50

    case units if units < 400:
        billamount = 100 * 3.00 + 100 * 3.50 + (units - 200) * 4.00

    case units if units < 700:
        billamount = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + (units - 400) * 4.50

    case _:
        billamount = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + (units - 700) * 5.00

print(f'Bill amount: Rs. {billamount:.2f}')
