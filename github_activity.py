import sys
import requests

if len(sys.argv) < 2:
    print("Uso: github_activity.py <command>")
    sys.exit(1)
else:
    user = sys.argv[1]

url = f"https://api.github.com/users/{user}/events"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(len(data))
elif response.status_code == 404:
    print(f"El usuario: {user} no existe.")
else:
    print(f"Hubo un error {response.status_code}.")
