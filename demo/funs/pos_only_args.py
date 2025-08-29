# positional-only args
def wish(message, name, /):
   print(message, name)


wish('Hi', 'Jason')
wish(name = 'Jason', message = 'Hello')

