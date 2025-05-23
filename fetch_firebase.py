import firebase_admin
from firebase_admin import credentials, firestore
import random
import pandas as pd

# Initialize Firebase
cred = credentials.Certificate('firebase_config.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
def fetch_firestore_data():
    doc_ref = db.collection("EspData").document("DHT11")
    doc = doc_ref.get()

    data = []

    if doc.exists:
        entry = doc.to_dict()
        print("Fetched entry:", entry)

        if 'Temperature' in entry and 'Humidity' in entry:
            temp_val = float(entry['Temperature'])
            hum_val = float(entry['Humidity'])

            # Generate similar random data
            for _ in range(100):
                temp = round(random.uniform(temp_val - 1, temp_val + 1), 2)
                hum = round(random.uniform(hum_val - 2, hum_val + 2), 2)
                data.append([temp, hum])
        else:
            print("⚠️ 'Temperature' or 'Humidity' fields missing in document.")
    else:
        print("⚠️ Document does not exist.")

    return pd.DataFrame(data, columns=["temperature", "humidity"])