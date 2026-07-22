import json
import os
import requests
from requests.auth import HTTPBasicAuth
from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("JIRA_EMAIL")
API_TOKEN = os.getenv("JIRA_API_TOKEN")

app = Flask(__name__)

JIRA_URL = "https://gagan7mn.atlassian.net/rest/api/3/issue"

auth = HTTPBasicAuth(EMAIL, API_TOKEN)

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}


@app.route("/createJira", methods=["POST"])
def createJira():

    data = request.get_json()

    print("=" * 60)
    print("GitHub Event Received")
    print("=" * 60)

    github_event = request.headers.get("X-GitHub-Event")

    print("Event :", github_event)

    # Only process issue comments
    if github_event != "issue_comment":
        return "Ignoring non issue_comment event", 200

    action = data.get("action")

    if action != "created":
        return "Ignoring edited/deleted comments", 200

    comment = data["comment"]["body"].strip()

    print("Comment :", comment)

    # Only trigger on /jira
    if comment.lower() != "/jira":
        return "Comment is not /jira", 200

    issue_title = data["issue"]["title"]
    issue_body = data["issue"]["body"] or "No description provided."
    github_issue_url = data["issue"]["html_url"]

    jira_payload = {
        "fields": {
            "project": {
                "key": "GAG"
            },
            "summary": issue_title,
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {
                                "type": "text",
                                "text": f"{issue_body}\n\nGitHub Issue: {github_issue_url}"
                            }
                        ]
                    }
                ]
            },
            "issuetype": {
                "name": "Bug"
            }
        }
    }

    # ================= DEBUG =================
    print("=" * 60)
    print("JIRA PAYLOAD")
    print("=" * 60)
    print(json.dumps(jira_payload, indent=4))
    # =========================================

    response = requests.post(
        JIRA_URL,
        headers=headers,
        auth=auth,
        data=json.dumps(jira_payload)
    )

    print("=" * 60)
    print("JIRA RESPONSE")
    print("=" * 60)
    print("Status Code :", response.status_code)
    print("Response Body:")
    print(response.text)

    if response.status_code == 201:
        print("Jira ticket created successfully.")
        return "Jira ticket created successfully", 201

    print("Jira ticket creation failed.")
    return response.text, response.status_code


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)