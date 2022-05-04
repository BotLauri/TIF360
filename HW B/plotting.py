import csv
import matplotlib.pyplot as plt

xValues = []
yValues = []
yValuesAvg = []

with open('Rewards_a.csv') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    x = 1
    for row in lines:
        xValues.append(x)
        yValues.append(float(row[0]))
        yValuesAvg.append(sum(yValues)/len(yValues)) # Moving average. 
        x += 1

plt.scatter(xValues, yValues, color = 'g', linestyle = 'dashed', marker = 'o', label = "Reward")
plt.plot(xValues, yValuesAvg, color = 'r', linestyle = 'dotted', marker = 'v', label = "Average reward")
  
plt.xlabel('Episode $E$')
plt.ylabel('Reward')
plt.title('Rewards as a function of Episode', fontsize = 20)
plt.grid()
plt.legend()
plt.show()
