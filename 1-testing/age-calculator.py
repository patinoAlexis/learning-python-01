
age = input("how old are you? \n")
# The double sign of // is making the number to be
# an int value
decades = int(age)//10
years = int(age)%10
print(" You are " + str(decades) + " decades old and " + str(years) + " years old")