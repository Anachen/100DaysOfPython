#DAY2
#22/04/2021
import matplotlib.pyplot as plt
import numpy as np

some_data = []
#Histogram withouth bin
plt.hist(some_data)

plt.show()
plt.clf() #cleans up
#Histogram with 5 bin
plt.hist(some_data,5)
plt.show()
plt.clf()
#LABELS and customisations
plt.plot(x_data,y_data,c=represents_color,alpha=0-1)
plt.xlabel('x label name')
plt.ylabel('y label name')
plt.title('Title of the Projection')
plt.yticks([0,2,4,6,8,10],['0','2B','4B','6B','8B','10B']) #Y label ticks and display name
plt.text(x_axis_place,y_axis_place,"some text")
plt.grid(True)
