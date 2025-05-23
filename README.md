A Mobile Unit for Weather Monitoring and Prediction using IoT and Machine Learning
This project combines real-time weather data collection via IoT (ESP8266 + DHT11 sensor) and predictive analytics using a Long Short-Term Memory (LSTM) neural network in Python. The system reads live data from Firebase Firestore, simulates historical data, trains an LSTM model, and visualizes both actual and predicted weather parameters (temperature & humidity).

🎯 Project Objectives
Develop a mobile unit equipped with DHT11 sensor for environmental data collection.

Stream real-time data to Firebase Firestore using ESP8266 (NodeMCU).

Use Python to fetch data, simulate historical trends, and train an LSTM model.

Predict future temperature and humidity.

Visualize results using matplotlib.

🧰 Technologies Used
Layer	Tools / Technologies
IoT Hardware	ESP8266 NodeMCU, DHT11 Temperature & Humidity Sensor
Backend	Firebase Firestore (Cloud)
Programming	C++ (ESP8266), Python (ML and plotting)
Libraries	tensorflow, sklearn, pandas, matplotlib, firebase-admin
ML Model	LSTM (Long Short-Term Memory)

📡 Firebase Setup
Create a Firebase project in the Firebase Console.

Go to Firestore Database → Start in test mode.

Create a collection: EspData

Add a document inside it: DHT11

Add fields:

Temperature: "25.80"

Humidity: "81.00"

Download the service account key JSON file:

Go to Project Settings → Service Accounts → Generate new private key.

Save it as firebase_config.json in your project directory.

📂 Project Structure
major_project/
│
├── firebase_config.json          # Firebase service account key
├── main.py                       # Main entry point
├── fetch_firestore.py            # Function to fetch & simulate data
├── lstm_model.py                 # LSTM training and prediction logic
├── requirements.txt              # Python dependencies

🧠 How It Works
ESP8266 pushes live temperature & humidity readings from DHT11 to Firestore.

main.py runs a Python pipeline that:

Reads the latest values from Firestore (EspData → DHT11).

Simulates 100 samples of synthetic historical data around the real-time value.

Trains an LSTM model using this synthetic time series.

Predicts the next temperature & humidity values.

Plots actual vs predicted values.


📈 Sample Output
Real-time value from Firebase:
Temperature = 25.80°C, Humidity = 81.00%

Plot:
A line chart showing the trend of generated historical data and predicted future values.

📊 Future Enhancements
Deploy the trained model to the ESP8266 (TinyML or Edge AI).

Use Realtime Database or Firestore with timestamp-based history.

Add GPS for mobile tracking of weather data.

Add LCD or OLED to display predictions on the device.

👨‍🎓 Project Members
Naman Kaushik (coding and building model) (2021335109)
Jayant Baisla (2021412704)

Final Year Student – CSE, Sharda University

📜 Acknowledgments
Firebase for real-time database support.

TensorFlow for LSTM modeling.
