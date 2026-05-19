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
    push_counts = {}
    messages = []
    for event in data:
        repo_name = event["repo"].get("name")
        if event["type"] == "PushEvent":
            push_counts[repo_name] = push_counts.get(repo_name, 0) + 1
    for k, v in push_counts.items():
        messages.append(f"Pushed {v} commits to {k}")
    for event in data:
        repo_name = event["repo"].get("name")
        action = event["payload"].get("action", "unknown")
        ref_type = event["payload"].get("ref_type", "unknown")
        if event["type"] == "CreateEvent":
            messages.append(f"Create a new {ref_type} in {repo_name}")
        elif event["type"] == "WatchEvent":
            messages.append(f"Starred {repo_name}")
        elif event["type"] == "IssuesEvent":
            messages.append(f"Issue {action} in {repo_name}")
    for message in messages:
        print(message)

elif response.status_code == 404:
    print(f"El usuario: {user} no existe.")
else:
    print(f"Hubo un error {response.status_code}.")
