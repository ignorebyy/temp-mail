from os import system as sy
try:
    from fake_email import Email
except ModuleNotFoundError:
    sy('pip install fake-email')

sy('clear')
print('Free temp-mail used pip module (fake-email)\nCreate By Kaeslva Ignorebyy')
mail = Email().Mail()
print('\nYour temp-mail : '+ mail['mail'])
print('Waiting Message...\n')
while True:
    mess = Email(mail['session']).inbox()
    if mess:
        print('From : '+ mess['from'] +' | '+ mess['name'])
        print('Subject : '+ mess['topic'])
        print('Message : '+ mess['message'])
        break
