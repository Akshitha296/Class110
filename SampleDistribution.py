import plotly.figure_factory as ff
import pandas as pd
import statistics
import random
import csv

df = pd.read_csv("newdata.csv")
data = df["average"].tolist()

data_mean = statistics.mean(data)
data_stdev = statistics.stdev(data)

print("Mean is ", data_mean)
print("Standard deviation is ", data_stdev)

def randomSetOfMeans(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data))
        value = data[random_index]
        dataset.append(value)
    sample_mean = statistics.mean(dataset)
    return sample_mean

def show_fig(mean_list):
    fig = ff.create_distplot([mean_list], ['average'], show_hist = False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0, 1000):
        setofmeans = randomSetOfMeans(100)
        mean_list.append(setofmeans)
    mean = statistics.mean(mean_list)
    sd = statistics.stdev(mean_list)
    print(mean)
    print(sd)
    show_fig(mean_list)

setup()