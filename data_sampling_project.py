import csv
import pandas as pd
import random
import statistics
import plotly.figure_factory as ff

#getting the reading time data from the csv and converting it to list
#creating a graph and showing it
df = pd.read_csv("/Users/Kartik/Downloads/medium_data.csv")
data = df["reading_time"].tolist()
fig = ff.create_distplot([data], ["reading_time"], show_hist=False)
fig.show()

#printing mean of the population data
print("population mean:- ",statistics.mean(data))

#getting random sets of means based on the number you gave
def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

#showing the graph of the data sampling
def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["reading_time"], show_hist=False)
    fig.show()

#giving counter value of 10
#calling random_set_of_means() 100 times and show_fig() once
def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means= random_set_of_mean(10)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    print("sampling mean:- ", statistics.mean(mean_list))
    
setup()

