
import requests

resp = requests.get("https://aisenseapi.com/services/v1/random_number/1/100")
print(resp.status_code)
data = resp.json()  # Convert respons in JSON to dict
print(data['random_number'])

