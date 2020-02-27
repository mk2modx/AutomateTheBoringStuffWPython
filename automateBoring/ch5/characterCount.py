import pprint

# pprint cleaner print display
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)  #character is the key and the it is defaulted to 0
    count[character] = count[character] + 1
    # count gets incremented everytime the key is found

pprint.pprint(count)