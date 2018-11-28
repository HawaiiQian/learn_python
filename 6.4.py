
spam='  Hello World !  '
print(spam.strip())
print(spam)
print(spam.lstrip()+'end')
print(spam.rstrip()+'end')

print('----------------------')

spam='SpamSpamspamEatEggspamSSamp'
print(spam.strip('mapS'))

print('----------------------')

import pyperclip
#pyperclip.copy('Hello!')
#print(pyperclip.paste())

print('----------------------')
'''
text=pyperclip.paste()
#print(text)
lines=text.split(' ')
for i in range(len(lines)):
    lines[i]='*'+lines[i]
print(text)
'''

