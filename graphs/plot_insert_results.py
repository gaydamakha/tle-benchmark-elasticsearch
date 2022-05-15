from cProfile import label
from numpy import *
import matplotlib.pyplot as plt

# MySQL Tests result
x=[100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600]
y1=[24.273, 22.293, 20.731, 19.923, 20.242, 20.052, 19.902, 19.922, 19.983]

# ElasticSearch Tests result
y2=[28.278, 27.896, 27.562, 26.816, 26.713, 26.066, 24.883, 25.535, 26.424]

plt.title('Data insertion comparison between ElasticSearch and MySQL')

plt.xlabel('Batch size (rows/docs)')
plt.ylabel('Time (sec)')

plt.plot(x, y1, 'r', label='MySQL') 
plt.plot(x, y2, 'b', label='ElasticSearch')

plt.legend(loc='upper center')

plt.show()