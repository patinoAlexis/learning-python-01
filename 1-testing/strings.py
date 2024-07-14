
# Inside python you can print a string in different ways
# or better said, you can put values inside a instri on different ways
# the most basic of them all is to concatenate strings

# Example 1:
# concatanation
print('Hello ' + 'World!')

# Example 2:
# using the format method
print('Hello {}'.format('World!'))

# Example 3:
# using f-strings
# this is a bit like in javascript, just with the additional f at the beginning
print(f'Hello World! ${1 + 1}')


# Example 4
# using templates strings
from string import Template
s = Template('$who likes $what')
print(s.substitute(who='Tim', what='kung pao'))