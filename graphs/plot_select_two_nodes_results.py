from numpy import *
import matplotlib.pyplot as plt

# 1 node search results
x=[100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600]
y1=[15, 29, 59, 129, 324, 514, 1076, 2179, 4755]

# 2 nodes search results
y2=[23,	37, 74, 156, 318, 629, 1296, 2662, 5462]

plt.title('ElasticSearch data search comparison with 1 node and 2 nodes')

plt.xlabel('Parallel queries number')
plt.ylabel('Time (ms)')

plt.plot(x, y1, 'r', label='1 node') 
plt.plot(x, y2, 'b', label='2 nodes')

plt.legend(loc='upper center')

plt.show()