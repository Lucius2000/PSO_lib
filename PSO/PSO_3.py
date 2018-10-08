#Particle Swarm Optimization written By Lucius
# Basic idea: Terminate optimization when the bias between the largest function value among
# all particles in the swarm and gBest is smaller than the preset terminate_value.

import random
import math
import numpy as np



# Function that we try to optimize (minimize)
def func(pos):
    return "blah"

# Cost function that calculate the current fitness
def costFunc():


#Class definition of a single particle
class Particle:

    def __init__(self, boundary, dim):
        self.velocity = np.array([], dtype=float64)
        self.position = np.array([], dtype=float64)
        # Personal Best Position
        self.pBest = np.array([], dtype=float64)
        # Function value of current position
        self.pValue = 0

        # Initialize position and velocity.
        for i in range(dim):
            self.velocity = numpy.append(self.velocity, random.uniform(-1, 1))
            self.position = numpy.append(self.position, random.uniform(boundary[i][0], boundary[i][1]))

        # Initialize pBest as the first position.
        self.pBest = self.position
        # Initialize first function value of first position.
        self.pValue = func(self.position)


    def position_update(self, boundary, func):
        # Update position
        self.position = self.position + self.velocity

        # Check for exceeding boundary's max end
        for j in range(dim):
            if self.position[j] > boundary[j][1]:
                self.position[j] = bouddary[j][1]
                self.velocity[j] = -1 * self.velocity[j]

        # Check for exceeding boundary's min end
        for k in range(dim):
            if self.position[k] < boundary[k][1]:
                self.position[k] = boundary[k][1]
                self.velocity[k] = -1 * self.velocity[k]

        # Update current function value of current position
        self.pValue = func(self.position)


    def velocity_update(self, gBest, v_Max):
        # Initialize parameters
        r1 = random.random()
        r2 = random.random()
        c1 = '%d'
        c2 = '%d'
        c3 = '%d'

        # Update velocity
        self.velocity = c1 * self.velocity + c2 * r1 * (self.pBest - self.position) + c3 * r2 * (gBest - self.pBest)

        # Check for exceeding max velocity
        for i in range(dim):
            if abs(self.velocity[i]) > v_Max:
                if self.velocity[i] >0:
                    self.velocity[i] = v_Max
                else:
                    self.velocity[i] = -1 * v_Max

    """""
    Evaluate function need some more scrunization
    """
    def self_evaluate(self, func):
        # Evaluate current position with all previous positions
        if func(self.position) < func(self.pBest):
            self.pBest = self.position
            self.pValue = func(self.position)





# ---------------------------- Class definition of PSO of a swarm ---------------------------#

class PSO():

    def __init__(self, boundary, particle_num, terminate_val):

        global dim
        dim = len(boundary)
        gBest = []                      # Initialize global best position
        g_Best_value = 0                # Initilize global best/smallest func value
        g_largest_bias = math.inf         # Initialize global largest bias between func value and g_Best_value
        vMax = 10

        # Initialize a swarm of particles
        swarm = []
        for i in range(particle_num):
            swarm.append(Particle[boundary, dim])

        # Get the first g_Best_value and g_largest_bias
        for i in range(particle_num):
            if swarm[i].pValue < g_Best_value or g_Best_value == 0:
                g_Best_value = swarm[i].pValue

        for i in range(particle_num):
            if swarm[i].pValue - g_Best_value > g_largest_bias or g_largest_bias == math.inf:
                g_largest_bias = swarm[i].pValue - g_Best_value

        for i in range(particle_num):
            swarm[i].position_update(boundary)
            swarm[i].velocity_update(gBest, vMax)


        # PSO optimization begins
        while g_largest_bias > terminate_val:
            for i in range(particle_num):
                swarm[i].self_evaluate()
                if swarm[i].pValue < g_Best_value:
                    gBest = swarm[i].position
                    g_Best_value = func(swarm[i].position)
                if swarm[i].pValue - g_Best_value > g_largest_bias:



            # Update velocity and position
            for i in range(particle_num):
                swarm[i].position_update(boundary)
                swarm[i].velocity_update(gBest, vMax)



if __name__ == "__PSO__":
        main()





#---------------------- Run the program -------------------------------------------------------------#
boundary = []
particle_num = '%d'
terminate_val = "%d"      # When the largest bias among all the biases (position - gBest)
                          # of particles is smaller than this terminate_err, we conclude that
                          # all particles have converged to the gBest point.