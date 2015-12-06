def poisson(lmbda,i):
    return lmbda ** i * math.e ** (-lmbda) /  math.factorial(i)

def NormalizedPoisson(lmbda,i):
    poissons = [poisson(lmbda,k) for k in range(i)]
    norm = sum(poissons)
    return [v / norm for v in poissons]

# This file was created for a live coding demo for my Game Theory class.
def Respond(lmbda,num_players):
    
