import random
from Creature import Creature

class Reproduce:
    # punnett square for the genes
    # random 0 to 2 to figure out how many offspring
    # create punnet square as list length 4
    # for each offspring
    #   random 0 to 3 to index into punnet square to select offspring
    #   add Offspring to offspring list
    # return offspring list
    def createOffsprings(self, creature1, creature2):
        offspring_num = random.randint(0,2)
        if offspring_num == 0:
            return []

        punnetSquare = [
            AllelePair(creature1.geneA, creature2.geneA),
            AllelePair(creature1.geneA, creature2.geneB),
            AllelePair(creature1.geneB, creature2.geneA),
            AllelePair(creature1.geneB, creature2.geneA)
        ]
        offspring_alleles = [punnetSquare[random.randint(0,3)] for i in range(offspring_num)]
        return [Creature(creature1.generation+1, a.allele_a, a.allele_b) for a in offspring_alleles]

    def __init__(self, creature1, creature2):
        self.creature1 = creature1
        self.creature2 = creature2
        self.offspring = self.createOffsprings(creature1, creature2)

    def __repr__(self):
        return f'Reproduce({self.creature1},{self.creature2},{self.offspring})'

class AllelePair:

    def __init__(self, allele_a, allele_b):
        self.allele_a = allele_a
        self.allele_b = allele_b