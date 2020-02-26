def spam():
    print(eggs) # ERROR unassigned
    eggs = 'spam local'

eggs = 'global'
spam()