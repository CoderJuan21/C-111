import csv
import plotly.figure_factory as ff
import pandas as pd
import statistics
import random
import plotly.graph_objs as go

df = pd.read_csv("Data.csv")

data = df["Math"].tolist()
#fig = ff.create_distplot([data], ["Math"], show_hist= False)
# fig.show()
mean = statistics.mean(data)
# sd = statistics.stdev(data)
# print("Mean is ====>", mean)
# print("StandDv is ====>", sd)

def random_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
mean_list = []
for i in range(0,1000):
    set_mean = random_mean(100)
    mean_list.append(set_mean)

mean = statistics.mean(mean_list)
sd = statistics.stdev(mean_list)
print("Mean is ====>", mean)
print("StandDv is ====>", sd)

# fig = ff.create_distplot([mean_list], ["Student Marks"], show_hist= False)
# fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.20], mode ="lines", name="MEAN"))
# fig.show()

first_sd_start, first_sd_end = mean - sd, mean + sd
second_sd_start, second_sd_end = mean -(2 * sd), mean +(2* sd)
third_sd_start, third_sd_end = mean -(3 * sd), mean +(3 * sd)

print("StandD1", first_sd_start, first_sd_end)
print("StandD2", second_sd_start, second_sd_end)
print("StandD3", third_sd_start, third_sd_end)

# fig = ff.create_distplot([mean_list], ["Student Marks"], show_hist= False)
# fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.20], mode ="lines", name="MEAN"))
# fig.add_trace(go.Scatter(x = [first_sd_start,first_sd_start], y = [0,0.20], mode ="lines", name="Sd one Start"))
# fig.add_trace(go.Scatter(x = [first_sd_end,first_sd_end], y = [0,0.20], mode ="lines", name="Sd one end"))
# fig.add_trace(go.Scatter(x = [second_sd_start,second_sd_start], y = [0,0.20], mode ="lines", name="Sd two Start"))
# fig.add_trace(go.Scatter(x = [second_sd_end,second_sd_end], y = [0,0.20], mode ="lines", name="Sd two end"))
# fig.add_trace(go.Scatter(x = [third_sd_start,third_sd_start], y = [0,0.20], mode ="lines", name="Sd 3 Start"))
# fig.add_trace(go.Scatter(x = [third_sd_end,third_sd_end], y = [0,0.20], mode ="lines", name="Sd 3 end"))
# fig.show()

# df = pd.read_csv("Data1.csv")
# data = df["Math"].tolist()
# meanS1 = statistics.mean(data)
# print("Mean is ====>", meanS1)

# fig = ff.create_distplot([mean_list], ["Student Marks"], show_hist= False)
# fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.20], mode ="lines", name="MEAN"))
# fig.add_trace(go.Scatter(x = [meanS1,meanS1], y = [0,0.20], mode ="lines", name="Mean of Sample 1"))
# fig.add_trace(go.Scatter(x = [first_sd_end,first_sd_end], y = [0,0.20], mode ="lines", name="Sd one end"))
# fig.show()
# z_score = (meanS1 - mean) / sd
# print("the Z score is ===>", z_score)

# df = pd.read_csv("Data2.csv")
# data = df["Math"].tolist()
# meanS2 = statistics.mean(data)
# print("Mean is ====>", meanS2)

# fig = ff.create_distplot([mean_list], ["Student Marks"], show_hist= False)
# fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.20], mode ="lines", name="MEAN"))
# fig.add_trace(go.Scatter(x = [meanS2,meanS2], y = [0,0.20], mode ="lines", name="Mean of Sample 2"))
# fig.add_trace(go.Scatter(x = [first_sd_end,first_sd_end], y = [0,0.20], mode ="lines", name="Sd one end"))
# fig.add_trace(go.Scatter(x = [second_sd_end,second_sd_end], y = [0,0.20], mode ="lines", name="Sd two end"))
# fig.show()
# z_score = (meanS2 - mean) / sd
# print("the Z score is ===>", z_score)

df = pd.read_csv("Data3.csv")
data = df["Math"].tolist()
meanS3 = statistics.mean(data)
print("Mean is ====>", meanS3)

fig = ff.create_distplot([mean_list], ["Student Marks"], show_hist= False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.20], mode ="lines", name="MEAN"))
fig.add_trace(go.Scatter(x = [meanS3,meanS3], y = [0,0.20], mode ="lines", name="Mean of Sample 2"))
fig.add_trace(go.Scatter(x = [first_sd_end,first_sd_end], y = [0,0.20], mode ="lines", name="Sd one end"))
fig.add_trace(go.Scatter(x = [second_sd_end,second_sd_end], y = [0,0.20], mode ="lines", name="Sd two end"))
fig.add_trace(go.Scatter(x = [third_sd_end,third_sd_end], y = [0,0.20], mode ="lines", name="Sd three end"))
fig.show()

z_score = (meanS3 - mean) / sd
print("the Z score is ===>", z_score)