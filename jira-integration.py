import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv
load_dotenv()

JIRA_API_URL = os.getenv("JIRA_API_URL")
API_TOKEN = os.getenv("JIRA_API_TOKEN")
EMAIL = os.getenv("JIRA_EMAIL")
ISSUE_ID = "DEV-1"

def get_jira_comments():
    url = JIRA_API_URL.format(issueIdOrKey="DEV-1")
    auth = HTTPBasicAuth(EMAIL, API_TOKEN)

    headers = {
       "Accept": "application/json"
    }

    response = requests.get(url, headers=headers, auth=auth)

    if response.status_code == 200:
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            print(f"Failed to decode JSON. Response content: {response.text}")
            return None
    else:
        print(f"Failed to fetch comments. Status code: {response.status_code}")
        print(f"Response content: {response.text}")
        return None
comments = get_jira_comments()
print(comments)