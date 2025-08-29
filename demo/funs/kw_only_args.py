# Keyword-only args
def wish(*, message = 'Hi', name):
   print(message, name)


#wish('Hi', 'Jason')
wish(name = 'Jason', message = 'Hello')
wish(name = "Scott")
