import numpy as np

"""
ODE of pendulum
theta_ddot = -g/1 * sin(theta)

Continuous state space model
x1 = theta
x2 = theta_dot
x1_dot = theta_dot = x2
x2_dot = theta_ddot = -g/l * sin(x1)

Discrete state space model
x1_k = x1_prev + x2_prev*Ts
x2_k = x2_prev + -g/l*sin(x1_prev)*Ts 


"""

