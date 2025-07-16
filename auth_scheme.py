import hashlib
import random
import time

def xor(a, b):
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b))

def hash_func(data):
    return hashlib.sha256(data.encode()).hexdigest()

def generate_random_key():
    return str(random.randint(100000, 999999))

class CentralAdministrator:
    def _init_(self):
        self.RU = generate_random_key()  
        self.RD = generate_random_key()  
        self.RG = generate_random_key() 

        self.user_store = {}
        self.device_store = {}
        print("\n--- System Initialization ---")
        print(f"RU (User Key): {self.RU}")
        print(f"RD (IoT Device Key): {self.RD}")
        print(f"RG (Gateway Key): {self.RG}")

    def register_user(self, user_id, password):
        random_key = generate_random_key()
        temp_id = hash_func(user_id + password + random_key)
        self.user_store[user_id] = {"temp_id": temp_id, "key": random_key}
        print("\n--- User Registration ---")
        print(f"User ID: {user_id}")
        print(f"Generated Random Key for User: {random_key}")
        print(f"Temporary ID for User: {temp_id}")
        return random_key, temp_id

    def register_device(self, device_id):
        random_key = generate_random_key()
        temp_id = hash_func(device_id + random_key)
        self.device_store[device_id] = {"temp_id": temp_id, "key": random_key}
        print("\n--- IoT Device Registration ---")
        print(f"IoT Device ID: {device_id}")
        print(f"Generated Random Key for Device: {random_key}")
        print(f"Temporary ID for IoT Device: {temp_id}")
        return random_key, temp_id

    def authenticate_user(self, user_id, received_temp_id, timestamp):
        print("\n--- User Authentication ---")
        if time.time() - timestamp > 30:  # Check if timestamp is within valid range
            print("Timestamp is expired!")
            return False
        stored_user = self.user_store.get(user_id)
        if stored_user and stored_user["temp_id"] == received_temp_id:
            print(f"User authenticated: {user_id}")
            return True
        print(f"User authentication failed for: {user_id}")
        return False

    def authenticate_device(self, device_id, received_temp_id, timestamp):
        print("\n--- IoT Device Authentication ---")
        if time.time() - timestamp > 30:
            print("Timestamp is expired!")
            return False
        stored_device = self.device_store.get(device_id)
        if stored_device and stored_device["temp_id"] == received_temp_id:
            print(f"IoT Device authenticated: {device_id}")
            return True
        print(f"IoT Device authentication failed for: {device_id}")
        return False

class User:
    def _init_(self, user_id, password, ca):
        self.user_id = user_id
        self.password = password
        self.ca = ca
        self.key = None
        self.temp_id = None

    def register(self):
        self.key, self.temp_id = self.ca.register_user(self.user_id, self.password)

    def login(self):
        timestamp = time.time()
        print(f"User attempting login with Temp ID: {self.temp_id} and Timestamp: {timestamp}")
        return self.ca.authenticate_user(self.user_id, self.temp_id, timestamp)

class IoTDevice:
    def _init_(self, device_id, ca):
        self.device_id = device_id
        self.ca = ca
        self.key = None
        self.temp_id = None

    def register(self):
        self.key, self.temp_id = self.ca.register_device(self.device_id)

    def authenticate(self):
        timestamp = time.time()
        print(f"IoT Device attempting authentication with Temp ID: {self.temp_id} and Timestamp: {timestamp}")
        return self.ca.authenticate_device(self.device_id, self.temp_id, timestamp)

if __name__ == "_main_":
    # Initialize Central Administrator (CA)
    ca = CentralAdministrator()

    # User registration and login
    user = User("user123", "password123", ca)
    user.register()
    if user.login():
        print("User authenticated successfully!")
    else:
        print("User authentication failed.")

    # IoT Device registration and authentication
    iot_device = IoTDevice("device123", ca)
    iot_device.register()
    if iot_device.authenticate():
        print("IoT Device authenticated successfully!")
    else:
        print("IoT Device authentication failed.")