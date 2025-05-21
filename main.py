from fastapi import FastAPI
import requests
import json
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "555Mix Viber Bot API is running"}

@app.post("/send-message")
def send_viber_message():
    url = "https://api.d7networks.com/viber/v1/send/"

    payload = json.dumps({
        "messages": [
            {
                "content": "Hello from 555Mix Football Bot!",
                "button_caption": "Join Now",
                "button_action": "https://www.ygnb2b.com",
                "recipients": ["+959788600011"],
                "label": "FOOTBALL"
            }
        ],
        "message_globals": {
            "originator": "555MIX",
            "call_back_url": "https://ygnb2b.com/viber-callback"
        }
    })

    headers = {
        'Authorization': f"Bearer {os.getenv('D7_API_TOKEN')}",
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload)
    return response.json()
