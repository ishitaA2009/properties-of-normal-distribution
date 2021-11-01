import csv
import random
import statistics
import plotly.figure_factory as ff

dice_result = []

for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    dice_result.append(dice1+dice2)

mean = sum(dice_result)/len(dice_result)
median = statistics.median(dice_result)
mode = statistics.mode(dice_result)
standardDeviation = statistics.stdev(dice_result)

print("Mean of this data is {}".format(mean))
print("Median of this data is {}".format(median))
print("Mode of this data is {}".format(mode))
print("Standard Deviation of this data is {}".format(standardDeviation))

fig = ff.create_distplot([dice_result],["result"],show_hist= False)
fig.show()