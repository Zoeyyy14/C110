import csv
import pandas as pd
import statistics
import plotly.figure_factory as ff
import random
import plotly.graph_objects as go

df=pd.read_csv("data.csv")
data=df["temp"].tolist()
#population_mean=statistics.mean(data)
#std_deviation=statistics.stdev(data)

#print("Population Mean Is:",population_mean)
#print("Population Standared Deviation Is:",std_deviation)
#fig=ff.create_distplot([data],["temp"],show_hist=False)
#fig.show()

# dataset=[]
# for i in range(0,100):
#     random_index=random.randint(0,len(data))
#     value=data[random_index]
#     dataset.append(value)
# mean=statistics.mean(dataset)
# std_deviation=statistics.stdev(dataset)
# print("Population Mean Is:",mean)
# print("Population Standared Deviation Is:",std_deviation)

def random_set_mean(c):
    dataset=[]
    for i in range(0,c):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def show_fig(mean_list):
   df=mean_list
   mean=statistics.mean(df)
   fig=ff.create_distplot([df],["temp"],show_hist=False)
   fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))
   fig.show()

def setup():
    mean_list=[]
    for i in range(0,1000):
        set_off_mean=random_set_mean(100)
        mean_list.append(set_off_mean)
    show_fig(mean_list)

setup()

mean=statistics.mean(data)
print("Mean of Sampling Destribution is:",mean)

def standared_deviation():
    mean_list=[]
    for i in range(0,1000):
        set_off_mean=random_set_mean(100)
        mean_list.append(set_off_mean)

    std_deviation=statistics.stdev(mean_list)
    print("Standared Deviation of Sampling Destribution is:",std_deviation)

standared_deviation()