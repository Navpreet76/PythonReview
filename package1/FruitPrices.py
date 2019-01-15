prices = {'Apple': 0.40, 'Banana': 0.50, 'Mango': 0.99, 'Pineapple': 1.29}
my_purchase = {
    'Apple': 1,
    'Banana': 12,
    'Mango': 4,
    'Pineapple': 2}
grocery_bill = sum(prices[fruit] * my_purchase[fruit]
                   for fruit in my_purchase)
print 'I owe the Grocer $%.2f' %grocery_bill