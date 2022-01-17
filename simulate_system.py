import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""
ODE of pendulum
theta_ddot = -g/l * sin(theta)

Continuous state space model
x1 = theta
x2 = theta_dot
x1_dot = theta_dot = x2
x2_dot = theta_ddot = -g/l * sin(x1)

Discrete state space model
x1_k = x1_prev + x2_prev*Ts
x2_k = x2_prev + -g/l*sin(x1_prev)*Ts 
"""

def sim_pendulum(l, Ts, tF, theta0):
    g = -9.8
    theta = [theta0]
    theta_dot = [0]
    iterations = int(np.round(tF/Ts))
    #print(iterations)
    #print(type(iterations))
    for k in range(1,iterations):
        theta.append(theta[k-1] + theta_dot[k-1]*Ts)
        theta_dot.append(theta_dot[k-1] + g/l*np.sin(theta[k-1]*Ts))

    return theta, theta_dot

l = 0.5
Ts = 0.00001
tF = 5
theta0 = np.pi/16
theta, thetadot = sim_pendulum(l, Ts, tF, theta0)
t = np.linspace(0, tF, int(np.round(tF/Ts)))
plt.plot(t, theta)
plt.show()

theta_df = pd.DataFrame(theta)
filename = 'real_data.csv'
theta_df.to_csv(filename)
