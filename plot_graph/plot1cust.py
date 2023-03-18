# plot a simple graph with customization
# we need matplotlib library to draw the graph in python..
import matplotlib.pyplot as plt

x=[1,4,7]
y=[2,3,6]
# x and y cordinates

plt.plot(x,y,color='green',linestyle='dashed',linewidth=3,marker='o',markerfacecolor='blue',markersize=12)

plt.ylim(1,8)
plt.xlim(1,8)

# label x and y aixis

plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.title("customized single line graph")

#to show the graph

plt.show()

