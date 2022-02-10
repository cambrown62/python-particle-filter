import pdb
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from params import *
import sys
import copy

class ParticleFilter:
    def __init__(self, Ts, theta0, theta_dot0=0, N=1000):
        self.num_particles = N
        self.particles = []
        self.theta_hat = theta0
        self.Ts = Ts
        self.weightsum = 0
        for i in range(self.num_particles):
            self.particles.append(Particle(theta0, theta_dot0, 1/N))

    def PropogateState(self):
        proc_stdev = np.sqrt(proc_cov)
        for particle in self.particles:
            theta_noise = np.random.normal(0, proc_stdev)
            theta_dot_noise = np.random.normal(0, proc_stdev)
            particle.theta = particle.theta_prev + particle.theta_dot_prev*self.Ts + theta_noise
            particle.theta_dot = particle.theta_dot_prev + g/l*np.sin(particle.theta_prev)*Ts + theta_dot_noise
            particle.theta_prev = particle.theta
            particle.theta_dot_prev = particle.theta_dot

    def CalcWeights(self, z):
        msmt_stdev = np.sqrt(msmt_cov)
        sum = 0
        for particle in self.particles:
            particle.weight = np.exp(-0.5 * (z - particle.theta)**2/msmt_stdev**2)/(msmt_stdev*np.sqrt(2*np.pi)) 
            sum += particle.weight

        self.weightsum = 0
        for particle in self.particles:
            particle.weight /= sum
            if particle.weight == 0:
                particle.weight = sys.float_info.epsilon
            self.weightsum += particle.weight 

    def EstimateState(self):
        EV = 0
        for particle in self.particles:
            EV += particle.weight * particle.theta
        self.theta_hat = EV
        
    def MultinomialResample(self):
        states_idx = []
        weights = []
        states = []
        for i in range(len(self.particles)):
            states_idx.append([self.particles[i].weight, i])
            weights.append(self.particles[i].weight)
        
        resamp_parts = []
        
        temp = np.random.multinomial(len(self.particles), weights)
        for i in range(len(temp)):
            for j in range(temp[i]):
                resamp_parts.append(copy.deepcopy(self.particles[i]))

        self.particles = resamp_parts
        

    def LowVarResample(self):
        r =  np.random.uniform()
        cumsum = 0
        resampled_particles = []
        idx = 0
        bounds = []
        for i in range(len(self.particles)):
            bounds.append([cumsum, cumsum+self.particles[i].weight])
            if r > bounds[i][0] and r < bounds[i][1]:
                idx = i
                resampled_particles.append(self.particles[i])
            cumsum += self.particles[i].weight

        interval = cumsum / self.num_particles 
        while len(resampled_particles) < self.num_particles:
            r += interval
            if r > bounds[idx][0] or r <= bounds[idx][1]:
                resampled_particles.append(self.particles[idx])
            else:
                idx += 1
            if idx > self.num_particles: 
                idx = 0
            
        self.particles = resampled_particles
            
    def RunFilter(self, z):
        self.PropogateState()
        self.CalcWeights(z)
        self.EstimateState()
        self.MultinomialResample()
        return self.theta_hat

class Particle:
    def __init__(self, theta0, theta_dot0, weight0):
        self.theta = self.theta_prev = theta0
        self.theta_dot = self.theta_dot_prev = theta_dot0
        self.weight = weight0

filename = 'measurement_data.csv'
z_df = pd.read_csv(filename)
z = z_df['0'].tolist()

pf = ParticleFilter(Ts, theta0, theta_dot0, num_particles)

theta_hat = []

for i in range(len(z)):
    theta_hat.append(pf.RunFilter(z[i]))

t = np.linspace(0, tF, len(theta_hat))
plt.plot(t, theta_hat)
plt.plot(t, z)
plt.show()

