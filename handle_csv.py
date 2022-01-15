#import csv
from random import sample
import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np

kf = 20
sample_freq = 2
num_samples = sample_freq*kf

x = np.linspace(0, kf, 10000)
y = []

for num in x:
    y.append(math.sin(num) + np.random.normal(0, 0.1))

'''
plt.plot(x,y)
plt.show()
'''

filename = 'measurement_data.csv'

y_df = pd.DataFrame(y)

y_df.to_csv(filename)

y_read = pd.read_csv(filename) 

#print(y_read)



'''
for i in range(len(y_read)):
    temp = y_read[i][0]
    del y_read[i]
    y_read[i] = temp
'''

#print(y_read[0][0])
#print(y_read[0])
'''
y_delta = []
for written, read in zip(y, y_read):
    y_delta.append(read - written)
    '''
#print(np.mean(y_delta))

