# 1 required, 1 optional
def wish(user, message = 'Hi'):
    print(message, user)

# Positional
#wish()
wish('Rossum')
wish('James', 'Good Morning')

# Keyword
wish(message="Hello", user='Larry')
wish(user = 'Scott')