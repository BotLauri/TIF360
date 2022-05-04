import csv
import matplotlib.pyplot as plt

xValues = []
yValues = []
yValuesAvg = []

with open('Rewards_c.csv') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    x = 1
    for row in lines:
        xValues.append(x)
        yValues.append(float(row[0]))
        yValuesAvg.append(sum(yValues[-100:])/len(yValues[-100:])) # SMA100. 
        x += 1

plt.scatter(xValues, yValues, color = 'b', marker = '|', label = "Reward")
plt.plot(xValues, yValuesAvg, color = 'r', linestyle = 'dashed', label = "SMA100")
  
plt.xlabel('Episode $E$')
plt.ylabel('Reward')
plt.title('Rewards as a function of Episode', fontsize = 20)
plt.grid()
plt.legend()
plt.show()
