import json
import sys
import urllib.request

def fetch_data(username):
    url = f"https://api.github.com/users/{username}/events"
    try:
        with urllib.request.urlopen(url) as responses:
            if responses.status == 200:
                data = json.load(responses)
                if not data:
                    print(f"No recent activity from this user{username}")
                    return
            print(f"Recent Activity of '{username}':")
            for event in data[:5]:
                event_type = event.get("type","Unkown Event")
                repo_name = event.get("repo",{}).get("name","Unkown Repo")
                action = parse_event(event_type)
                print(f"- {action} {repo_name}")
            else:
                print(f"Error : Received status Code {responses.status}")

    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("Error : User not found.")
        else:
            print(f"HTTP Error :{e.code}")
    except urllib.error.URLError:
        print("Error : Failed to fetch data .Check your internet connection.")

def parse_event(event_type):
    event_map = {
        "PushEvent": "Pushed commits to",
        "PullRequestEvent": "Opened a pull request in",
        "IssuesEvent": "Opened a new issue in",
        "ForkEvent": "Forked",
        "WatchEvent": "Starred",
    }
    return event_map.get(event_type, event_type.replace("Event", " in"))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: github-activity <username>")
        sys.exit(1)

    username = sys.argv[1]
    fetch_data(username)
