def wish(user, message):
    print(message, user)

# Positional
wish('Rossum', 'Hi')
wish('James', 'Good Morning')
wish(10, 20)

# Keyword
wish(message="Hello", user='Larry')

