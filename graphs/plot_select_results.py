from cProfile import label
from numpy import *
import matplotlib.pyplot as plt

# MySQL Tests result
x=[100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600]
y1=[0.137, 0.115, 0.088, 0.080, 0.115, 0.136, 0.119, 0.148, 0.205]

# ElasticSearch Tests result
y2=[15, 29, 59, 129, 324, 514, 1076, 2179, 4755]

plt.title('Data search comparison between ElasticSearch and MySQL')

plt.xlabel('Parallel queries number')
plt.ylabel('Time (ms)')

plt.plot(x, y1, 'r', label='MySQL') 
plt.plot(x, y2, 'b', label='ElasticSearch')

plt.legend(loc='upper center')

plt.show()