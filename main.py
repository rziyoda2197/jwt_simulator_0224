import base64
import json

def create_token(payload):
    data = json.dumps(payload).encode()
    return base64.urlsafe_b64encode(data).decode()

def decode_token(token):
    data = base64.urlsafe_b64decode(token.encode())
    return json.loads(data)

user = {"username": "admin"}

token = create_token(user)
print("Token:", token)

print("Decoded:", decode_token(token))
