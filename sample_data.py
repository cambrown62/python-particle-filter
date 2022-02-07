import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from params import *

def sample_data(data, sample_rate, msmt_cov, Ts):
    out = []
    i = 0
    while i < len(data):
        out.append(data[i]+np.random.normal(0, msmt_cov))
        i += int(sample_rate/Ts)
    return out

filename = 'real_data.csv'
theta_df = pd.read_csv(filename)
theta = theta_df['0'].tolist()
#Ts = 0.00001
#tF = 5
#sample_rate = Ts*1000
#cov = 0.03
z = sample_data(theta, Ts, msmt_cov, Ts_sim)
#print(len(z))
t = np.linspace(0,tF,len(z))
plt.plot(t, z)
plt.show()

theta_df = pd.DataFrame(z)
filename = 'measurement_data.csv'
theta_df.to_csv(filename)