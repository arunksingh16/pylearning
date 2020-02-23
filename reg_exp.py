import re

string1 = 'Hi this is a this string.'

print('this' in string1)
x =re.search('this', string1)
print(x)


pattern = re.compile('this')
y=pattern.search(string1)
print(y)
