# drawing bar chart in python

import matplotlib.pyplot as plt

left = [3,4,5,6,7]
height = [12,30,20,21,7]

bar_titles = ['o','t','th','f','fi']

plt.bar(left,height,tick_label=bar_titles,width=0.8,color=['red','orange'])

# label x and y aixis

plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.title("Bar chart")

#to show the graph
plt.show()