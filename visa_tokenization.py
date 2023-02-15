#SCIAT FREE-CODEY

import requests
import json

def main():
    # Sandbox Server address
    url = 'https://sandbox.api.visa.com/cofds-web/v1/datainfo'

    # Sample data request: This is the payload that we will send to the Sandbox Server
    payload = {
        "requestHeader": {
            "requestMessageId": "6da6b8b024532a2e0eacb1af58581",
            "messageDateTime": "2019-02-35 05:25:12.327"
        },
        "requestData": {
            "pANs": [
                "4072208010000000"
            ],
            "group": "STANDARD"
        }
    }

    # Load configuration data
    config = load_config('config.json')
    user_id = config["user_id"]
    password = config["password"]
    cert_path = config["cert_path"]
    key_path = config["key_path"]

    timeout = 10

    # Send request to server
    try:
        response = requests.post(url,
                                 cert=(cert_path, key_path),
                                 auth=(user_id, password),
                                 json=payload,
                                 timeout=timeout)

        # Print response data
        print(response.headers)
        print(response.content)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def load_config(config_path):
    with open(config_path) as config_file:
        return json.load(config_file)

if __name__ == '__main__':
    main()
