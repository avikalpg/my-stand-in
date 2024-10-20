import requests
from requests.auth import HTTPBasicAuth

JIRA_API_URL = "https://mystandin.atlassian.net/browse/DEV-1?focusedCommentId=10002"
API_TOKEN = "ATATT3xFfGF09OrT2Kqo3dcLyMw3NPZ-k2a_my9UNCoqDWfwWW4RtfYjRT1vGlwSKr0O-jh-kENoSUBPd5sLC1rUihNVgVH4ttIq-hM8Fd3-SArCXUOtsrQjiN5PNMtgQufZSPj-1_PSYwZ9bxnSm7djVnCa7zRRj02_VCKiOH95CvIU0sL_VHc=0EA8ACADen"
EMAIL = "sabh619@gmail.com"
ISSUE_ID = "DEV-1"

def get_jira_comments():
    url = JIRA_API_URL.format(issueIdOrKey="DEV-1")
    auth = HTTPBasicAuth(EMAIL, API_TOKEN)
    
    headers = {
       "Accept": "application/json"
    }

    response = requests.get(url, headers=headers, auth=auth)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch comments: {response.status_code}")
        return None

comments = get_jira_comments()
print(comments)


https://mystandin.atlassian.net/browse/DEV-1