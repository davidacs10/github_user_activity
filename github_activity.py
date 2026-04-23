import sys

if len(sys.argv) < 2:
    print("Uso: github_activity.py <command>")
    sys.exit(1)
else:
    print(sys.argv[1])
