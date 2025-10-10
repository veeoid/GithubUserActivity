import argparse
# from api_endpoint import getUserData
from default_api_endpoint import get_userdata as get

def main():
    parser = argparse.ArgumentParser(description='Will parse CLI for Github User')
    parser.add_argument('username')
    parser.add_argument('filter', choices=['commits', 'pull_requests', 'issues', 'all'], default='all', nargs='?')

    args = parser.parse_args()
    userdata = get(args.username)
    filter = args.filter

    for event in userdata:
        if filter == 'all':
            print(f'{event["type"]}: {event["repo"]["name"]} at {event["created_at"]}')
        elif filter == 'commits' and event['type'] == 'PushEvent':
            print(f'Commit: {event["repo"]["name"]} at {event["created_at"]}')
        elif filter == 'pull_requests' and event['type'] == 'PullRequestEvent':
            print(f'Pull Request: {event["repo"]["name"]} at {event["created_at"]}')
        elif filter == 'issues' and event['type'] == 'IssuesEvent':
            print(f'Issue: {event["repo"]["name"]} at {event["created_at"]}')
        


if __name__ == '__main__':
    main()