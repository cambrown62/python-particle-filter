import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from params import *

def sample_data(data, sample_rate, msmt_cov, Ts):
    out = []
    real = []
    i = 0
    while i < len(data):
        real.append(data[i])
        out.append(data[i]+np.random.normal(0, msmt_cov))
        i += int(sample_rate/Ts)
    return out, real

filename = 'real_data.csv'
theta_df = pd.read_csv(filename)
theta = theta_df['0'].tolist()
z, real = sample_data(theta, Ts, msmt_cov, Ts_sim)
'''
t = np.linspace(0,tF,len(z))
plt.plot(t, z, '*')
plt.plot(t, real, '*')
plt.show()
'''
theta_df = pd.DataFrame({"z": z, "real": real})
filename = 'measurement_data.csv'
theta_df.to_csv(filename)