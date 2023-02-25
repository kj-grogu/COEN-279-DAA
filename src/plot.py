
import matplotlib.pyplot as plt

listx = [10, 20, 30, 40]
xaxis = listx

# Y axis parameter:
listy = [999, 99, 99, 9]
yaxis = listy


plt.xlabel("I am x")
plt.ylabel("I am y")
plt.title("With Labels")
plt.plot(xaxis, yaxis, linestyle='--', marker='o', color='b', label='line with marker')
plt.legend()
plt.show()