# A Mobile Unit for Weather Monitoring and Prediction using IoT and Machine Learning

This project combines real-time weather data collection via IoT (ESP8266 + DHT11 sensor) and predictive analytics using a Long Short-Term Memory (LSTM) neural network in Python. The system reads live data from Firebase Firestore, simulates historical data, trains an LSTM model, and visualizes both actual and predicted weather parameters (temperature & humidity).

## 🌟 Project Objectives

- Develop a mobile unit equipped with DHT11 sensor for environmental data collection.
- Stream real-time data to Firebase Firestore using ESP8266 (NodeMCU).
- Use Python to fetch data, simulate historical trends, and train an LSTM model.
- Predict future temperature and humidity.
- Visualize results using matplotlib.

---

## 🧰 Technologies Used

| Layer           | Tools / Technologies                              |
|----------------|----------------------------------------------------|
| IoT Hardware   | ESP8266 NodeMCU, DHT11 Temperature & Humidity Sensor |
| Backend        | Firebase Firestore (Cloud)                        |
| Programming    | C++ (ESP8266), Python (ML and plotting)           |
| Libraries      | tensorflow, sklearn, pandas, matplotlib, firebase-admin |
| ML Model       | LSTM (Long Short-Term Memory)                     |

---

## 📱 Firebase Setup

1. Create a Firebase project in the Firebase Console.
2. Go to Firestore Database → Start in test mode.
3. Create a collection: `EspData`
4. Add a document inside it: `DHT11`
5. Add fields:
   - `Temperature`: "25.80"
   - `Humidity`: "81.00"
6. Download the service account key JSON file:
   - Go to Project Settings → Service Accounts → Generate new private key.
   - Save it as `firebase_config.json` in your project directory.

---

## 📂 Project Structure

```
major_project/
│
├── firebase_config.json          # Firebase service account key
├── main.py                       # Main entry point
├── fetch_firestore.py            # Function to fetch & simulate data
├── lstm_model.py                 # LSTM training and prediction logic
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

---

## 🧠 How It Works

1. ESP8266 pushes live temperature & humidity readings from DHT11 to Firestore.
2. `main.py` runs a Python pipeline that:
   - Reads the latest values from Firestore (`EspData` → `DHT11`).
   - Simulates 100 samples of synthetic historical data around the real-time value.
   - Trains an LSTM model using this synthetic time series.
   - Predicts the next temperature & humidity values.
   - Plots actual vs predicted values.

---

## 🚀 How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Ensure `firebase_config.json` is in your project root.
3. Run the pipeline:

```bash
python main.py
```

4. You will see:
   - Data fetched from Firestore
   - LSTM model training progress
   - A matplotlib graph of actual vs predicted values

---

## 📊 Sample Output

- Real-time value from Firebase:  
  Temperature = 25.80°C, Humidity = 81.00%

- Plot:  
  A line chart showing the trend of generated historical data and predicted future values.

---

## 📊 Future Enhancements

- Deploy the trained model to the ESP8266 (TinyML or Edge AI).
- Use Realtime Database or Firestore with timestamp-based history.
- Add GPS for mobile tracking of weather data.
- Add LCD or OLED to display predictions on the device.

---

## 👨‍🎓 Project Members

- Naman Kaushik (created the code and model) (2021335109)
- B.Tech CSE (AIML)
- Final Year Student – Sharda University, Greater Noida

---

## 📜 Acknowledgments

- Firebase for real-time database support.
- TensorFlow for LSTM modeling.
- OpenAI & ChatGPT for technical assistance.
