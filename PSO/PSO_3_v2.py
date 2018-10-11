#Particle Swarm Optimization written By Lucius
# Basic idea: Terminate optimization when the bias between the largest function value among
# all particles in the swarm and gBest is smaller than the preset terminate_value.

import random
import math
import numpy as np



# Function that we try to optimize (minimize)
def func(pos):
    return pos[0]**2


# Class definition of Particle
class Particle:

    def __init__(self, boundary, vmax):
        self.velocity = np.array([], dtype="float64")
        self.position = np.array([], dtype="float64")
        # Personal Best Position
        self.pBest = np.array([], dtype="float64")
        # Function value of current position
        self.pValue = 0
        self.dim = len(boundary)
        self.vmax = vmax

        # Initialize position and velocity.
        for i in range(self.dim):
            self.velocity = np.append(self.velocity, random.uniform(-1, 1))
            self.position = np.append(self.position, random.uniform(boundary[i][0], boundary[i][1]))

        # Assign pBest's first position.
        self.pBest = self.position
        # Assign pValue's first value.
        self.pValue = func(self.position)


    def position_update(self, boundary, func):
        # Update position
        self.position = self.position + self.velocity


        # Check for exceeding boundary's max end
        for j in range(self.dim):
            if self.position[j] > boundary[j][1]:
                self.position[j] = boundary[j][1]
                self.velocity[j] = -1 * self.velocity[j]

        # Check for exceeding boundary's min end
        for k in range(self.dim):
            if self.position[k] < boundary[k][1]:
                self.position[k] = boundary[k][1]
                self.velocity[k] = -1 * self.velocity[k]

        # Update current function value of current position
        self.pValue = func(self.position)


    def velocity_update(self, gBest):
        # Initialize parameters
        r1 = random.random()
        r2 = random.random()
        c1 = 0.1
        c2 = 0.1
        c3 = 0.1


        # Update velocity
        self.velocity = c1 * self.velocity + c2 * r1 * (self.pBest - self.position) + c3 * r2 * (gBest - self.pBest)

        # Check for exceeding max velocity
        for i in range(self.dim):
            #v_i = abs(self.velocity[i])
            if abs(self.velocity[i]) > self.vmax:
                if self.velocity[i] > 0:
                    self.velocity[i] = self.vmax
                else:
                    self.velocity[i] = -1 * self.vmax

    # Evaluate current position with all previous positions
    def self_evaluate(self, func):
        if func(self.position) < func(self.pBest):
            self.pBest = self.position






# ---------------------------- Class definition of PSO of a swarm ---------------------------#

#class PSO():

#   def __init__(self, boundary, particle_num, terminate_val):

def pso(boundary, particle_num, terminate_val):

        global dim
        dim = len(boundary)
        gBest = []                      # Initialize global best position
        g_Best_value = 0                # Initilize global best/smallest func value
        g_largest_bias = math.inf         # Initialize global largest bias between func value and g_Best_value
        #vMax = 0.5
        iter = 1

        print("Start!\n")
        # Initialize a swarm of particles
        swarm = []
        for i in range(particle_num):
            swarm.append(Particle(boundary, dim))


        """""
        NEED MORE SCRUTINY AT THE FIRST ONE/TWO STEPS AFTER THE INITIALIZATION
        """
        # Get the first g_Best_value and g_largest_bias
        for i in range(particle_num):
            if swarm[i].pValue < g_Best_value or g_Best_value == 0:
                g_Best_value = swarm[i].pValue

        for i in range(particle_num):
            if swarm[i].pValue - g_Best_value > g_largest_bias or g_largest_bias == math.inf:
                g_largest_bias = swarm[i].pValue - g_Best_value

        for i in range(particle_num):
            swarm[i].position_update(boundary, func)
            # swarm[i].velocity_update(gBest, vMax)


        # PSO optimization begins
        while g_largest_bias > terminate_val:
            print("Round: ", iter, "\n")
            for i in range(particle_num):
                if swarm[i].pValue < g_Best_value:
                    gBest = swarm[i].position
                    g_Best_value = func(swarm[i].position)

            g_largest_bias = swarm[0].pValue - g_Best_value

            for i in range(1, particle_num):
                if swarm[i].pValue - g_Best_value > g_largest_bias:
                    g_largest_bias = swarm[i].pValue - g_Best_value


            # Update velocity and position
            for i in range(particle_num):
                swarm[i].self_evaluate(func)
                swarm[i].velocity_update(gBest, vMax)
                swarm[i].position_update(boundary, func)

            iter += 1

        print("Best position is: ", gBest, "Best_value is: ", g_Best_value)



#---------------------- Run the program -------------------------------------------------------------#
boundary = [[-100,100]]
particle_num = 30
terminate_val = 0.0000001       # When the largest bias among all the biases (position - gBest)
                                # of particles is smaller than this terminate_err, we conclude that
                                # all particles have converged to the gBest point.
p1 = Particle(boundary, 0.5)
v = p1.velocity
p1.position_update(boundary, func)
p1.velocity_update(boundary)
print(p1.velocity)


#pso(boundary, particle_num, terminate_val)
