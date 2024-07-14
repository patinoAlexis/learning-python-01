
# Getting the data
moneyOwed = float(input('How much money do you owe, in dollars?\n')) # $50,000

apr = 0.03 # 3%
payment = float(input('How much will you pay each month?\n')) # $1,000
months = int(input('How many months will it take to pay off the loan?\n')) # 24

# Calculate the data
monthlyRate = apr/12
for i in range(months):
    interestPaid = moneyOwed * monthlyRate
    moneyOwed += interestPaid
    moneyOwed -= payment
    if moneyOwed < 0:
        moneyOwed = 0
        print(f'The lasy payment was {moneyOwed + payment}')
        print(f'You paid off the loan in {i+1} months!')
        break
    # Output the data
    print(f'Paid {payment} of which {interestPaid} was interest')
    print(f'Now i owe {moneyOwed}')


