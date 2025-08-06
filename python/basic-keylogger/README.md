# Simple Keylogger (Practice)

This folder contains two Python scripts demonstrating a basic keylogger setup for educational purposes. **This is for practice and learning only and should not be used maliciously.**

## Files

* `cliente.py`: This script captures keyboard input and sends it to a specified server.
* `servidor.py`: This script acts as a server, receives key presses from `cliente.py`, and logs them to a file.

## How it Works

1.  **`cliente.py` (Client - Keylogger)**:
    * Uses the `keyboard` library to listen for key press events.
    * When a key is pressed, it sends the key's name as a JSON payload to the `servidor.py` using an HTTP POST request.
    * The `server_url` is set to `http://localhost:5000/key`, indicating it expects the server to be running locally on port 5000.
    * It continues to capture and send keys until the 'esc' key is pressed.

2.  **`servidor.py` (Server - Key Receiver)**:
    * Built with the `Flask` web framework.
    * Exposes a `/key` endpoint that listens for POST requests.
    * When a request is received, it extracts the `key` value from the JSON data.
    * It then prints the received key to the console and appends it to a file named `keys_register.txt`.
    * Returns a JSON response indicating success.

## Setup and Usage

### Prerequisites

* Python 3.x
* `keyboard` library (`pip install keyboard`)
* `requests` library (`pip install requests`)
* `Flask` library (`pip install Flask`)

### Running the Application

1.  **Start the Server:**
    Open a terminal and run the server script:
    ```bash
    python servidor.py
    ```
    You should see output similar to:
    ```
     * Serving Flask app 'servidor'
     * Debug mode: off
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
     * Running on [http://0.0.0.0:5000](http://0.0.0.0:5000)
    Press CTRL+C to quit
    ```

2.  **Start the Client:**
    Open *another* terminal and run the client script:
    ```bash
    python cliente.py
    ```
    You will see messages like "Sending key: [key_name]" as you type.

3.  **Type and Observe:**
    Now, type anything while the `cliente.py` script is running.
    * In the terminal running `servidor.py`, you will see "key pressed: [key_name]" for each key you type.
    * A file named `keys_register.txt` will be created (or updated) in the same directory as `servidor.py`, containing a log of all pressed keys.

4.  **Stop the Client:**
    Press the `esc` key in the terminal where `cliente.py` is running to stop the key capture.

5.  **Stop the Server:**
    Press `CTRL+C` in the terminal where `servidor.py` is running to stop the Flask server.

## Important Note

This project is intended solely for educational purposes to understand how basic keylogging and network communication can be implemented. **Using such a script without explicit permission on a system you do not own is illegal and unethical.** Always ensure you have the necessary authorization before deploying or testing any form of monitoring software.
