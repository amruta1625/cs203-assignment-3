import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def simulate(n, k, samples):
    same_choice_wins = 0
    switched_choice_wins = 0
    for __ in range(samples):
        doors = ["car"] * k + ["goat"] * (n - k)
        random.shuffle(doors)
        ind = np.arange(0,n)

        # Players choice
        first_choice = np.random.choice(ind)

        # The host now opens one of the unchosen doors that contains goat
        if(len([x for x in ind if x != first_choice and doors[x]=="goat"])==0):
            return 1, 1
        show = np.random.choice([x for x in ind if x != first_choice and doors[x]=="goat"])

        # First case when the player does not switch
        if(doors[first_choice]=="car"):
            same_choice_wins+=1
        
        # Second case when the player switches
        second_choice = np.random.choice([x for x in ind if x!=first_choice and x!=show])
        if(doors[second_choice]=="car"):
            switched_choice_wins+=1
    
    return same_choice_wins, switched_choice_wins

# Number of doors
n_values = np.arange(3, 20)

# Number of cars
k_values = np.arange(1, 18)

# Number of samples
samples = 10000

# Perform the simulation for all combinations of n and k
X, Y = np.meshgrid(n_values, k_values)
size = X.shape[0]
win1 = np.zeros(size)
win2 = np.zeros(size)
Hratio = np.zeros((size, size))
for i in range(size):
    for j in range(size):
        result = simulate(X[i][j], Y[i][j], samples)
        win1[i] += result[1]
        win2[i] += result[0]
        if win2[i] == 0:
            Hratio[i, j] = 100000000000
        else:
            Hratio[i, j] = win1[i] / win2[i]

# Plot the results
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Hratio, cmap="YlOrBr")
ax.set_xlabel("Number of cars(k)")
ax.set_ylabel("Number of doors(n)")
ax.set_zlabel("P(win|W) / P(win|T)")
plt.title("Variation of P(win|W)/P(win|T) with n and k")
plt.show()