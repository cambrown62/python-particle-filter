import particle_filter as pf
import matplotlib.pyplot as plt
import pandas as pd
from params import *
import numpy as np

filename = 'measurement_data.csv'
df = pd.read_csv(filename)
z = df['z'].tolist()
real = df['real'].tolist()

pf1 = pf.ParticleFilter(Ts, theta0, theta_dot0, num_particles)

theta_hat = []

for i in range(len(z)):
    theta_hat.append(pf1.RunFilter(z[i]))

msmt_rmse = np.sum((np.square(np.subtract(real, z))))/len(z)
theta_hat_rmse = np.sum((np.square(np.subtract(real, theta_hat))))/len(z)
print("msmt_rmse: " + str(msmt_rmse))
print("theta_hat_rmse: " + str(theta_hat_rmse))

t = np.linspace(0, tF, len(theta_hat))
plt.plot(t, theta_hat, '*', label='theta hat')
plt.plot(t, z, '*', label='measured')
plt.plot(t, real, '*', label='real')
plt.legend()
plt.show()