import random


def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    if answerNumber == 2:
        return 'It is decidedly so'
    if answerNumber == 3:
        return 'Yes'
    if answerNumber == 4:
        return 'Reply hazy try again'
    if answerNumber == 5:
        return 'Ask again later'
    if answerNumber == 6:
        return 'Concentrate and ask again later'
    if answerNumber == 7:
        return 'My reply is No'
    if answerNumber == 8:
        return 'Outlook not so good'
    if answerNumber == 9:
        return 'Very Doubtful'


r = random.randint(1, 9)  # pick a number between 1 and 9
fortune = getAnswer(r)
print(fortune)

# OR

print(getAnswer(random.randint(1, 9)))