

print("enter a number :")
number = input()
number = int(number)


def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2

    elif number % 2 == 1:
        result = (3 * number + 1)
        print(result)
        return int(result)


while number != 1:
    number = collatz(number)



