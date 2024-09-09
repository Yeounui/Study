class Population():
    def __init__(self, m=0, n=0, k=0):
        # Definition
        self.m = m
        self.n = n
        self.k = k
        self.population = [1] * m + [2] * n + [3] * k
        self.encounters = 0

    def __str__(self):
        return "type I: {}, type II: {}, type III: {} (after {} encounters)" \
            .format(self.m, self.n, self.k,
                    self.encounters
                    )

    def __repr__(self):
        return "Population({}, {}, {})".format(self.m, self.n, self.k)

    def plasmids(self):
        return tuple((self.m, self.n, self.k))

    def size(self):
        return self.m + self.n + self.k

    def encounter(self, i, j):
        # encounters attribute counts
        self.encounters += 1

        # If two locus have different number, a change executes.
        if self.population[i] != self.population[j]:

            # Figure out what number would be replaced.
            case = {1, 2, 3}
            case.remove(self.population[i])
            case.remove(self.population[j])
            case = case.pop()

            # Change m, n, k values
            if case == 1:
                self.m += 2
                self.n -= 1
                self.k -= 1

            elif case == 2:
                self.m -= 1
                self.n += 2
                self.k -= 1

            else:
                self.m -= 1
                self.n -= 1
                self.k += 2

            # Replace each value of locus with another number.
            self.population[i] = case
            self.population[j] = case


import random


def simulation(population, number=1, display=1):

    print(population)

    # Repeat "number" times.
    i = 0
    while i != number:
        # Choice two random locus in the population
        bac_i, bac_j = random.choices(range(population.size()),
                                      k=2)
        # Execute encounter
        population.encounter(bac_i, bac_j)

        # Show the progress at an initial moment and every multiple of "display".
        if population.encounters % display == 0:
            print(population)

        i += 1



population = Population(m=998, n=1, k=1)
print(population)
print(repr(population))
print(population.plasmids())
print()
for i in range(population.size() - 1):
    population.encounter(i, i + 1)
print(population)
for i in range(population.size() - 1):
    population.encounter(i, i + 1)
print(population)

population = Population(m=998, n=1, k=1)
simulation(population, 10000, 250)