import numpy as np

g = -9.8            # gravity
l = 0.5             # length of pendulum
Ts_sim = 0.00001    # sample time for ZOH sim of pendulum
Ts = Ts_sim*1000    # sample time for sampling data
tF = 5              # length of time to sim pendulum
theta0 = np.pi/16   # initial theta of pendulum   
theta_dot0 = 0      # initial angular velocity of pendulum
msmt_cov = 0.03     # covariance of measurement data
proc_cov = 0.07     # covariance of process
num_particles = 100  # number of particles
