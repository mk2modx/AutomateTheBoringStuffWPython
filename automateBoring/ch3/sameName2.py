def spam():
    global eggs    # this refers to the global version of eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)