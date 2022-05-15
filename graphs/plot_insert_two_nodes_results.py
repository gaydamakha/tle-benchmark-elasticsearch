from cProfile import label
from numpy import *
import matplotlib.pyplot as plt

# 1 node insert results
x=[100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600]
y1=[28.278, 27.896, 27.562, 26.816, 26.713, 26.066, 24.883, 25.535, 26.424]

# 2 nodes insert results
y2=[27.205, 26.223, 25.505, 27.127, 27.021, 25.544, 26.157, 24.490, 26.779]

plt.title('ElasticSearch data insertion comparison with 1 node and 2 nodes')

plt.xlabel('Batch size (rows/docs)')
plt.ylabel('Time (sec)')

plt.plot(x, y1, 'r', label='1 node') 
plt.plot(x, y2, 'b', label='2 node')

plt.legend(loc='upper center')

plt.show()