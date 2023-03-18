# plot a simple graph 
# we need matplotlib library to draw the graph in python..
import matplotlib.pyplot as plt

x=[1,4,7]
y=[2,3,6]
# x and y cordinates

plt.plot(x,y)

# label x and y aixis

plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.title("single line graph")

#to show the graph

plt.show()

