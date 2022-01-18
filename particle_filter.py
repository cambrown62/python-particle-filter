import numpy as np
import matplotlib.pyplot as plt

class ParticleFilter:
    def __init__(self, theta0, N=1000):
        self.num_particles = N
        self.particles = []
        self.theta_hat = theta0
        for i in range(self.num_particles):
            self.particles.append(Particle(theta0, 1/N))

    def PropogateState():
        for particle in self.particles:
            particle.theta = theta_prev

class Particle:
    def __init__(self, theta0, weight):
        self.theta = self.theta_prev = theta0
        self.weight = weight



#pf = ParticleFilter(np.pi/16, 100)