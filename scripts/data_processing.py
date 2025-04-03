import pandas as pd
from matplotlib import pyplot as plt

def plot_data(data, mean, xlabel, ylabel, output_plot_file):
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.plot(data, "r-")
    plt.axhline(y=mean, color="b", linestyle="--")
    plt.show()
    plt.savefig(output_plot_file)
    plt.clf()

def get_data(file, column, num_rows):
    data = pd.read_csv(file, nrows=num_rows)
    return data[column]

def compute_mean(data):
    return sum(data) / len(data)