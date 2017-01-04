# Kate Archer
# Exercise 5

noShares = float(input("Enter number of shares:"))
purPrice = float(input("Enter purchase price:"))
salPrice = float(input("Enter sale price:"))

amountPaid = purPrice * noShares

broker1 = amountPaid * 0.03

totalInvest = amountPaid + broker1

amountSold = noShares * salPrice

broker2 = amountSold * 0.03

totalSale = amountSold - broker2

Net = totalSale - totalInvest

if (Net >= 0):
    print('After the transaction, you gained', Net, 'dollars.')
else:
    print('After the transaction, you lost', (Net * -1), 'dollars.')
