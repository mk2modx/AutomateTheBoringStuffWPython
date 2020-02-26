print("What's your name?")
name = input()
print("And how old are you?")
age = input()
age = int(age)

if name == 'Alice':
    print('Hi, Alice.')

elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('Tou are not Alice, grannie.')