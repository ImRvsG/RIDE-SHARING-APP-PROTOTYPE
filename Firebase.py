import firebase_admin
from firebase_admin import credentials, firestore
import requests

# Firebase Setup
cred = credentials.Certificate("path/to/firebase-sdk.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Function to request a ride
def request_ride(user_id, pickup, dropoff):
    ride_data = {
        "user_id": user_id,
        "pickup_location": pickup,
        "dropoff_location": dropoff,
        "status": "pending"
    }
    db.collection("rides").add(ride_data)
    return "Ride requested successfully!"

# Google Maps API for location tracking (Replace API_KEY)
def get_distance(pickup, dropoff):
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={pickup}&destination={dropoff}&key=API_KEY"
    response = requests.get(url).json()
    distance = response["routes"][0]["legs"][0]["distance"]["text"]
    return distance
