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

print('-------------------------------')

spam='Hello'.rjust(10,'+')
print(spam)
spam='Hello'.ljust(20,'-')
print(spam)
spam='Hello'.center(10,'=')
print(spam)

print('-------------------------------')

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k,v in itemsDict.items():
        print(k+str(v))
things={'apple':5,'banner':20,'oranger':10}
print(printPicnic(things,10,20))

print('-------------------------------')
'''
left=10
right=20
print('PICNIC ITEMS'.center(left+right,'-'))
print(len('PICNIC ITEMS'.center(left+right,'-')))

'''

things={'apple':5,'banner':20,'oranger':10}

def pp(itemsDict,left,right):
    for k,v in itemsDict.items():
        print(k.ljust(left,'*')+str(v).rjust(right,'-'))
pp(things,10,20)