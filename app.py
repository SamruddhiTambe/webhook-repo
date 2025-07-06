from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from datetime import datetime
import os

app = Flask(__name__)

MONGO_URI = "mongodb+srv://webhook_user:webhook123@cluster0.inuh89h.mongodb.net/webhook_data?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI)
db = client["webhook_data"]
collection = db["events"]

@app.route('/webhook', methods=['POST'])
def webhook():
    event_type = request.headers.get('X-GitHub-Event')
    data = request.json

    # Initializing fields
    action = ""
    author = ""
    from_branch = ""
    to_branch = ""
    timestamp = datetime.utcnow().strftime("%d %B %Y - %I:%M %p UTC")
    request_id = ""

    if event_type == "push":
        action = "PUSH"
        author = data["pusher"]["name"]
        from_branch = None
        to_branch = data["ref"].split("/")[-1]
        request_id = data["after"]

        message = f'"{author}" pushed to "{to_branch}" on {timestamp}'

    elif event_type == "pull_request":
        author = data["pull_request"]["user"]["login"]
        from_branch = data["pull_request"]["head"]["ref"]
        to_branch = data["pull_request"]["base"]["ref"]
        request_id = str(data["pull_request"]["id"])

        if data["action"] == "opened":
            action = "PULL_REQUEST"
            message = f'"{author}" submitted a pull request from "{from_branch}" to "{to_branch}" on {timestamp}'
        elif data["action"] == "closed" and data["pull_request"]["merged"]:
            action = "MERGE"
            message = f'"{author}" merged branch "{from_branch}" to "{to_branch}" on {timestamp}'
        else:
            return jsonify({"status": "ignored"}), 200

    else:
        return jsonify({"status": "ignored"}), 200

    entry = {
        "request_id": request_id,
        "author": author,
        "action": action,
        "from_branch": from_branch,
        "to_branch": to_branch,
        "timestamp": timestamp,
        "message": message,
    }

    collection.insert_one(entry)
    return jsonify({"status": "saved", "message": message}), 200

# @app.route('/webhook', methods=['POST'])
# def webhook():
#     data = request.json
#     print(" Webhook payload received:")
#     print(data)
#     return {"status": "received"}, 200

@app.route('/events', methods=['GET'])
def get_events():
    events = list(collection.find().sort("_id", -1).limit(10))
    return jsonify([e["message"] for e in events])

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=5000)
