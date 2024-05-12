import requests

# Configuration
rabbitmq_url = 'http://10.105.180.222:15672'
username = 'guest'  # Default username; change as needed
password = 'guest'  # Default password; change as needed
payload_size = 5000000  # Size of the payload in bytes

# Crafting a large message
message = {
    "properties": {},
    "routing_key": "test",
    "payload": "A" * payload_size,  # Repeat 'A' to create a large message
    "payload_encoding": "string"
}

# Headers
headers = {'content-type': 'application/json'}

# Send the request
response = requests.post(rabbitmq_url, json=message, auth=(username, password), headers=headers)

# Output the response
print('Status Code:', response.status_code)
print('Response:', response.text)
