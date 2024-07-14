# The main difference between conditionals on python that are on other languages
# is that in python, you have the keyword 'or' instead of || and 'and' instead of &&

# Example 1
temperature = 75
if temperature > 70 and temperature < 80:
    print("It's a nice day")
else:
    print('It is not a nice day');

# Example 2
# There is also no need to add the add statement in some cases, the next code
# is the same as the previous one

if 70 < temperature < 80:
    print("It's a nice day")
else:
    print('It is not a nice day');

# Example 3
if temperature < 70 or temperature > 80:
    print("It's not a nice day")
else:
    print('It is a nice day');

# also instead of using ! to negate a condition, we use in python the keyword not
# Example 4
if not temperature < 70:
    print("It's a nice day")
else:
    print('It is not a nice day');

