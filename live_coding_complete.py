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
def Respond(lmbda,num_players,level):
    if level == 0:
        return (50,[50])
    else:
        probs = NormalizedPoisson(lmbda,level)
        (a,responses) = Respond(lmbda,num_players,level - 1)
        avg = sum([probs[i] * responses[i] for i in range(0,level)])
        play = PlayAverage(num_players,avg)
        return (play,responses + [play])

def PlayWithPlayers(num_players,lmbda):
    ls = []
    for i in range(0,num_players):
        (a,b) = Respond(lmbda,num_players,AssignLevel(lmbda,num_players))
        ls = ls + [a]
    return sum(ls) / len(ls)
