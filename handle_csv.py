import csv
import math
import matplotlib.pyplot as plt
import numpy as np

func_range = 100

x = np.linspace(0, 20, 10000)
y = []

for num in x:
    y.append(math.sin(num) + np.random.normal(0, 0.1))

'''
plt.plot(x,y)
plt.show()
'''

filename = 'measurement_data.csv'

with open(filename, 'w') as f:
    write = csv.writer(f)
    for val in y:
        write.writerow([val])

y_read = []

with open(filename, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        y_read.append(row)

#print(y_read)

y_delta = np.subtract(np.array(y), np.array(y_read))

'''
y_delta = []
for written, read in zip(y, y_read):
    y_delta.append(read-written)
'''
print(np.mean(y_delta))

