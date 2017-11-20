import numpy as np
import math
import random
import itertools


def populate():
    population = np.empty([8, 8], dtype=np.ndarray)
    for (x, y), element in np.ndenumerate(population):
        population[x][y] = np.around(((np.random.rand(8,8))*100), 5)in
    return population

def tournament(population):
    #Testing mechanism to bring population to median as proof of concept of evaluation of population.
    holdingPopulation = np.empty([8, 8], dtype=np.ndarray)
    scoringMechanism = np.empty([8, 8], dtype=int)
    for (x, y), element in np.ndenumerate(scoringMechanism):
        scoringMechanism[x][y] = 50
    tournament = ([x for x in itertools.product(range(8), range(8))])
    #ENTER THUNDERDOME
    Results = []
    while len(tournament) != 1:
        entrantOne = random.choice(tournament)
        tournament= [x for x in tournament if x != entrantOne]
        entrantTwo = random.choice(tournament)
        tournament = [x for x in tournament if x != entrantTwo]
        #Start of evaluation mechanic. Placeholder representing the optimum median value of an 8x8 grid initialized between 0,100
        if abs(50 - np.average(population[entrantOne])) <  abs(np.average(50-(population[entrantTwo]))):
            Victor = entrantOne
            Results.append(entrantTwo)
        else:
            Victor = entrantTwo
            Results.append(entrantOne)
        tournament.append(Victor)
    Results.append(tournament[0])
    while len(Results) != 0:
        for (x, y), element in np.ndenumerate(holdingPopulation):
            holdingPopulation[x][y] = population[Results.pop()]
    return holdingPopulation

def breed(resultList, population):
    newGeneration = np.empty([8, 8], dtype=np.ndarray)
    breedingPairs = ([x for x in itertools.product(range(4, 8), range(8))]), ([x for x in itertools.product(range(4, 8), range(8))])
    for x in range(8):
        for y in range(4):
            newGeneration[x][y] = population[x][y]
    for x in range(8):
        for y in range(4,8):
            parent1, parent2 = random.choice(breedingPairs[0]), random.choice(breedingPairs[1])
            newGeneration[x][y] = mate(population[parent1], population[parent2])
    return newGeneration

def mate(entrantOne, entrantTwo):
    inheritance = [entrantOne, entrantTwo]
    progeny = np.empty([8, 8], dtype=float)
    for (x, y), element in np.ndenumerate(progeny):
        #May revise later, not mendelian, straight 50/50. May have to rely on fixation of strong characteristics much harder than is healthy for population.
        gene = random.choice(inheritance)
        progeny[x][y] = np.around(gene[x][y], 5)
    return progeny

# print(type(np.around(((np.random.rand(8,8))*100), 5)))
population = populate()
for x in range(100000):
    newGen = None
    results = tournament(population)
    newGen = breed(results, population)
    print(50 - np.average(np.average(newGen)))
