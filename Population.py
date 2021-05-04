from Creature import Creature

class Population:
    def __init__(self, creatures):
        self.size = len(creatures)
        genoType_count = countByGenoType(creatures)
        self.percA = genoType_count['A']/self.size
        self.percB = genoType_count['B']/self.size
        self.percMix = genoType_count['Mix']/self.size
        self.creatures = creatures

    def __repr__(self):
        return f'Population({self.size},{self.percA},{self.percB},{self.percMix})'

def countByGenoType(creatures):
    genoTypes = { 'A': 0, 'B': 0, 'Mix': 0 }
    for creature in creatures:
        if creature.geneA == 'A' and creature.geneB == 'A':
            genoTypes['A'] += 1
        elif creature.geneA == 'B' and creature.geneB == 'B':
            genoTypes['B'] += 1
        else:
            genoTypes['Mix'] += 1
    return genoTypes

def populateGeneration(gen_num, size, percA, percB, percMix):
    sizeA = int(size*percA)
    sizeB = int(size*percB)
    sizeMix = size*percMix
    pop = []
    pop = [Creature(gen_num, 'A', 'A') for i in range(sizeA)]
    pop += [Creature(gen_num, 'B', 'B') for i in range(sizeB)]
    pop += [Creature(gen_num, 'A', 'B') for i in range(int(sizeMix/2))]
    pop += [Creature(gen_num, 'B', 'A') for i in range(int(sizeMix/2))]
    return pop





