import sys
import requests

if len(sys.argv) < 2:
    print("Uso: github_activity.py <command>")
    sys.exit(1)
else:
    user = sys.argv[1]

url = f"https://api.github.com/users/{user}/events"
response = requests.get(url)
