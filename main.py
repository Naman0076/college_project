from fetch_firebase import fetch_firestore_data
from lstm_model import train_and_predict
from plot_graph import plot_results

def main():
    df = fetch_firestore_data()
    predicted, actual = train_and_predict(df)
    plot_results(predicted, actual)

if __name__ == "__main__":
    main()
