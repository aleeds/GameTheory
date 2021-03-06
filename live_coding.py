import math
import random as rand

def poisson(lmbda,i):
    return lmbda ** i * math.e ** (-lmbda) /  math.factorial(i)

def AssignLevel(lmbda,level):
    distr = NormalizedPoisson(lmbda,level)
    dens = 0
    for i in range(len(distr)):
        dens += distr[i]
        if rand.random() < dens:
            return i
    return len(distr) - 1

def NormalizedPoisson(lmbda,i):
    poissons = [poisson(lmbda,k) for k in range(i)]
    norm = sum(poissons)
    return [v / norm for v in poissons]

def PlayAverage(num_players,avg):
    return 2 * avg * (num_players - 1) / (3 * num_players - 2)

# This file was created for a live coding demo for my Game Theory class.
  

def PlayWithPlayers(num_players,lmbda):
