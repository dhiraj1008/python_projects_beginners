# draw two lines on a graph

# we need matplotlib library to draw the graph in python..
import matplotlib.pyplot as plt

x1=[1,4,7]
y1=[2,3,6]
x2=[3,7,8]
y2=[4,7,9]
# x and y cordinates

plt.plot(x1,y1,label='line 1')
plt.plot(x2,y2,label='line 2')
# label x and y aixis

plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# to differentiate two lines
plt.legend()

#to title the graph
plt.title("single line graph")

#to show the graph

plt.show()

