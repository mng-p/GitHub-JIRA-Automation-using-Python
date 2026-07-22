# GitHub-JIRA-Automation-using-Python

Automatically create Jira tickets from GitHub Issue comments using **GitHub Webhooks**, **Python Flask**, and the **Jira REST API**.

---

# 📌 Project Overview

This project demonstrates an end-to-end automation where GitHub communicates with Jira through a Python Flask application.

Whenever a user comments:

```text
/jira
```

on a GitHub Issue, GitHub triggers a webhook to the Flask application. The application validates the comment, extracts the GitHub issue details, and creates a Jira Bug using the Jira REST API.

This project demonstrates integration between GitHub, Python, REST APIs, and Jira.

---

# 🛠 Tech Stack

- Python
- Flask
- GitHub Webhooks
- Jira REST API
- REST APIs
- Ubuntu EC2
- Linux
- Git
- JSON

---

# 🔄 Workflow

```text
                GitHub Issue

                     │
                     ▼

             Comment "/jira"

                     │
                     ▼

            GitHub Webhook Event

                     │
                     ▼

         Python Flask Application

                     │
                     ▼

           Validate Comment

                     │
                     ▼

           Build JSON Payload

                     │
                     ▼

           Jira REST API

                     │
                     ▼

           Jira Bug Created
```

---

# ✨ Features

- GitHub Webhook Integration
- Flask REST Endpoint
- Automatic Jira Ticket Creation
- REST API Integration
- JSON Payload Creation
- HTTP Basic Authentication
- Comment Validation (`/jira`)
- Error Handling
- Detailed Logging
- Real-time Automation

---

# 📂 Project Structure

```text
GitHub-JIRA-Automation-using-Python/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── screenshots/
│   ├── jira-ticket-created.png
│   ├── ec2-terminal-output.png
│   └── webhook-response.png
└── architecture.png
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/<your-github-username>/GitHub-JIRA-Automation-using-Python.git
```

Go to the project directory

```bash
cd GitHub-JIRA-Automation-using-Python
```

Create Virtual Environment

```bash
python3 -m venv venv
```

Activate Virtual Environment

### Linux / Ubuntu

```bash
source venv/bin/activate
```

### Windows

```cmd
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
python app.py
```

The Flask server starts on

```text
http://<EC2-Public-IP>:5000/createJira
```

---

# 📋 How It Works

1. Create a GitHub Issue.
2. Add the comment:

```text
/jira
```

3. GitHub sends an **issue_comment** webhook.
4. Flask receives the webhook.
5. Flask validates the `/jira` command.
6. Flask extracts the GitHub Issue Title and Description.
7. Flask creates a JSON payload.
8. Flask calls the Jira REST API.
9. Jira creates a Bug automatically.

---

# 💻 Sample Output

```text
============================================================
GitHub Event Received
============================================================

Event : issue_comment

Comment : /jira

Jira Status : 201

Jira ticket created successfully
```

---

# 📸 Screenshots

## 1️⃣ Jira Ticket Created

The Jira backlog showing the bug automatically created from the GitHub issue comment.

```markdown
![Jira Ticket Created](screenshots/jira-ticket-created.png)
```

---

## 2️⃣ Flask Application Running on EC2

Shows the Flask application receiving the GitHub webhook and successfully creating the Jira ticket.

```markdown
![EC2 Terminal Output](screenshots/ec2-terminal-output.png)
```

---

## 3️⃣ GitHub Webhook Delivery

Shows GitHub successfully delivering the webhook and receiving HTTP 201 from the Flask application.

```markdown
![GitHub Webhook](screenshots/webhook-response.png)
```

---

# 🏗 Architecture

```text
                    GitHub

                       │

                       ▼

             GitHub Webhook

                       │

                       ▼

          Python Flask Application
               (Ubuntu EC2)

                       │

                       ▼

             Jira REST API

                       │

                       ▼

              Jira Bug Created
```

---

# 🔐 Security

For security reasons, API Tokens and Email IDs should never be hardcoded.

Instead, use:

- Environment Variables
- `.env`
- AWS Secrets Manager (Production)

Example:

```python
EMAIL = os.getenv("JIRA_EMAIL")
API_TOKEN = os.getenv("JIRA_API_TOKEN")
```

---

# 📚 Future Improvements

- Create Jira Story, Task, and Epic
- Prevent Duplicate Jira Tickets
- Update GitHub Issue with Jira Ticket Link
- Deploy using Docker
- Deploy with Kubernetes
- CI/CD using GitHub Actions
- Unit Testing
- Logging using Prometheus & Grafana

---

# 👨‍💻 Author

**Gagan**

DevOps Engineer | Python | AWS | Docker | Kubernetes | Terraform | GitHub Actions

---
