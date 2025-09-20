import requests

resp = requests.get("https://api.github.com/users/gvanrossum")
if resp.status_code != 200:
    print('Sorry! Could not get details!')
    exit()

data = resp.json()
print('Name      : ', data['name'])
print('Company   : ', data['company'])
print('Location  : ', data['location'])