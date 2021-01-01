#Develop Discount Calculator App
purchases_amount = int(input('purchases_amount:'))
if purchases_amount <= 1000:
    print('Total Bill:', purchases_amount)
elif purchases_amount >= 1001 & purchases_amount <=2000:
    discount = (purchases_amount/100*10)
    print('discount:', discount)
    bill = purchases_amount - discount
    print('Total Bill:', bill)
elif purchases_amount >= 2001 & purchases_amount <= 3000:
    discount = (purchases_amount / 100 * 20)
    print('discount:', discount)
    bill = purchases_amount - discount
    print('Total Bill:', bill)
elif purchases_amount > 3001 :
    discount = (purchases_amount / 100 * 25)
    print('discount:', discount)
    bill = purchases_amount - discount
    print('Total Bill:', bill)

