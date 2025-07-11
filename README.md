#  webhook-repo: Flask Webhook Receiver + MongoDB + UI

- ﻿Flask app to receive GitHub webhooks and store/display in MongoDB

This repository contains a **Flask application** that receives GitHub webhook events from `action-repo`, stores them in **MongoDB Atlas**, and displays them on a simple **auto-refreshing UI**.

---

##  Purpose

This is built to:

1. Receive GitHub events (`push`, `pull_request`, and `merge`)
2. Save event data to MongoDB in a clean format
3. Show updates on a minimal UI that refreshes every 15 seconds

---

##  Folder Structure
webhook-repo/
│
├── app.py # Flask backend to handle incoming GitHub webhook
├── templates/
│ └── index.html # Frontend for UI rendering GitHub event messages
├── static/
│ └── script.js # JS for polling MongoDB every 15 seconds
└── README.md # This file


---

##  Setup Instructions

### 1. Install Dependencies

```bash
pip install flask pymongo
```

### 2. Start the Flask App
```bash
python app.py
```

### 3. Expose Flask App via ngrok
```bash
ngrok config add-authtoken <your-auth-token>
ngrok http 5000
``` 
Copy the generated https://xxxx.ngrok-free.app and set it as the Webhook Payload URL on GitHub:
```bash
https://xxxx.ngrok-free.app/webhook
```

### MongoDB Schema
Each GitHub event is stored in this format:
```bash
{
  "request_id": "commit_or_pr_id",
  "author": "username",
  "action": "PUSH / PULL_REQUEST / MERGE",
  "from_branch": "source_branch",
  "to_branch": "target_branch",
  "timestamp": "formatted UTC time",
  "message": "final message displayed on UI"
}
```
### Web UI Features
Displays the latest 10 GitHub events

UI updates every 15 seconds

Minimal, clean layout using plain HTML/CSS/JS

✅ Events Captured & Displayed
Event Type	Format Example
```bash
Push	"SamruddhiTambe" pushed to "main" on 06 July 2025 - 04:15 PM UTC
Pull Request	"SamruddhiTambe" submitted a pull request from "dev" to "main" on ...
Merge	"SamruddhiTambe" merged branch "dev" to "main" on ...
```

##  Testing Done
- Push event tested

- Pull Request event tested

- Merge event tested

- MongoDB shows saved events

- UI renders and updates automatically

## Notes
- UI is kept minimal for readability

- Used beginner-level Python and JavaScript for maintainability

- MongoDB Atlas used for hosted DB access

## Linked Repositories
- Webhook Source: [action-repo](https://github.com/SamruddhiTambe/action-repo.git)

## Assignment Checklist
 1. Flask app with MongoDB integration

 2. GitHub webhook configured

 3. Push / PR / Merge events saved to DB

 4. UI with polling every 15 seconds

 5. Clean code and readable format

 6. Final README submitted
