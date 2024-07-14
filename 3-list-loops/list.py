

# Creating a list
listOne = ['LOL', 'OMG' 'LMFAO']
print(listOne)
# To add new items
listOne.append('WTF')
print(listOne)

# To remove items
listOne.remove('LOL')
print(listOne)

# We can check if certain items are on the list
# using the if statement and 'in' keyword
if 'OMG' in listOne:
    print('OMG is in the list')
else:
    print('OMG is not in the list')