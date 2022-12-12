blocks = int(input('How many blocks? '))
prices = [0.08, 0.12, 0.04, 0.02, 1.20]
total = float(0)

for price in prices:
    subtotal = float(blocks * price)
    total = total + subtotal

print('Total price = €%.2f' % total)