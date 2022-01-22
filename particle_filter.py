import numpy as np
import matplotlib.pyplot as plt
from params import *

class ParticleFilter:
    def __init__(self, Ts, theta0, theta_dot0=0, N=1000):
        self.num_particles = N
        self.particles = []
        self.theta_hat = theta0
        self.Ts = Ts
        for i in range(self.num_particles):
            self.particles.append(Particle(theta0, theta_dot0, 1/N))

    def PropogateState(self):
        for particle in self.particles:
            particle.theta = self.theta_prev + self.theta_dot_prev*self.Ts + proc_cov
            particle.theta_dot = self.theta_dot_prev + g/l*np.sin(self.theta_prev)*Ts + proc_cov

    def CalcWeights(self, z):
        msmt_stdev = np.sqrt(msmt_cov)
        sum = 0
        for particle in self.particles:
            particle.weight = np.exp(-0.5 * (z - particle.theta)^2/msmt_stdev^2)/msmt_stdev/np.sqrt(2*np.pi) 
            sum += particle.weight
        
        for particle in self.particles:
            particle.weight /= sum

    def EstimateState(self):



class Particle:
    def __init__(self, theta0, theta_dot0, weight0):
        self.theta = self.theta_prev = theta0
        self.theta_dot = self.theta_dot_prev = theta_dot0
        self.weight = weight0



#pf = ParticleFilter(np.pi/16, 100)