__author__ = 'Jano'

#
# onemax.py - useage example
#
# the fittest individual will have a chromosome consisting of 30 '1's
#

import genetic

class OneMax(genetic.Individual):
    optimization = genetic.MAXIMIZE
    def evaluate(self, optimum=None):
        self.score = sum(self.chromosome)
    def mutate(self, gene):
        self.chromosome[gene] = not self.chromosome[gene] # bit flip

if __name__ == "__main__":
    env = genetic.Environment(OneMax, maxgenerations=1000, optimum=30)
    env.run()
