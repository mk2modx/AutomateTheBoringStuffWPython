def spam(divideBy):
    try: # try clause
        return 42 / divideBy
    except ZeroDivisionError: # except clause
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
