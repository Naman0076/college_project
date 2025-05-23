import matplotlib.pyplot as plt

def plot_results(predicted, actual):
    plt.figure(figsize=(10, 5))
    plt.plot(actual, label='Actual')
    plt.plot(predicted, label='Predicted')
    plt.title("LSTM Prediction vs Actual")
    plt.xlabel("Time")
    plt.ylabel("Temperature")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
