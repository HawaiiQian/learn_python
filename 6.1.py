def spam():
    '''Dear Hawaii,
    Good day!
    Sincerely,
    Bai'''
print('Hello!')

print('-------------------------------')

spam='Hello World'
print(spam[0])
print(spam[-1])
print(spam[:5])

print('-------------------------------')

spam='Hello' in 'Hello World'
print(spam)
spam='cats' not in 'cats and dogs'
print(spam)

print('-------------------------------')
'''
print("How are you?")
feeling=input()
if feeling.lower()=='great':
    print('I am fine too.')
else:
    print('I am so sorry.')
'''

print('-------------------------------')

spam='I am Fine.'
print(spam.lower())
print(spam.upper())

print('-------------------------------')

spam='ABC'
print(spam.islower())
print(spam.isupper())

print('-------------------------------')

print('abc'.isalpha())
print('abc123'.isalnum())
print('abc123-'.isalnum())
print('This abc.'.istitle())

print('-------------------------------')

'''
while True:
    print('Enter your age:')
    age=input()
    if age.isdecimal():
        break;
    print('Please enter a number for your age.')
while True:
    print('Select a new password (letters and numbers only):')
    password=input()
    if password.isalnum():
        break;
    print('letters and numbers only')
'''

print('-------------------------------')

spam='Hello World!'.startswith('Hel')
print(spam)
spam='Hello World!'.endswith('!')
print(spam)

print('-------------------------------')

spam='and'.join(['Bob ',' Lucy ',' Hawaii'])
print(spam)
spam='+'.join(['Alice','Bob','Patty'])
print(spam)
spam='My name is LiLei'.split()
print(spam)
spam='XX+XXX+XXXX'.split('+')
print(spam)
