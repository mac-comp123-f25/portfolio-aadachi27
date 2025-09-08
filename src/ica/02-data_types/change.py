# calculate change in specific bills and coins to give back to someone

money = 8937 # amount in cents

print('Change for', money, 'cents:')
dollars = money // 100
print('Dollars:', dollars)
quarters = (money % 100) // 25
print('Quarters:', quarters)
dimes = ((money % 100) - (25 * quarters)) // 10
print('Dimes:', dimes)
nickels = ((money % 100) - (25 * quarters) - (10 * dimes)) // 5
print('Nickels:', nickels)
pennies = ((money % 100) - (25 * quarters) - (10 * dimes) - (5 * nickels))
print('Pennies:', pennies)