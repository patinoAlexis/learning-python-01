

expenses = [10.50, 8, 5, 15, 20, 5, 3]

sumVal = 0

for x in expenses:
    sumVal += x


print(f'You spent ${sumVal} on lunch this week.')

# we can also use the built-in sum() function to calculate the sum of the list
total = sum(expenses)
print(f'You spent ${total} on lunch this week.')
