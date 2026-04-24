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
    for event in data:
        repo_name = event["repo"].get("name")
        action = event["payload"].get("action", "unknown")
        ref_type = event["payload"].get("ref_type", "unknown")
        if event["type"] == "PushEvent":
            print(f"Pushed commits to {repo_name}")
        elif event["type"] == "CreateEvent":
            print(f"Create a new {ref_type} in {repo_name}")
        elif event["type"] == "WatchEvent":
            print(f"Starred {repo_name}")
        elif event["type"] == "IssuesEvent":
            print(f"Issue {action} in {repo_name}")
elif response.status_code == 404:
    print(f"El usuario: {user} no existe.")
else:
    print(f"Hubo un error {response.status_code}.")
