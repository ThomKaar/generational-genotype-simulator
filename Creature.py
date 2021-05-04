class Creature:

    maxId = 0

    def __init__(self, generation, geneA, geneB, partner=None):
        self.id = Creature.maxId
        Creature.maxId += 1
        self.generation = generation
        self.geneA = geneA
        self.geneB = geneB
        self.partner = partner

    def __repr__(self):
        return f'Blob({self.id},{self.generation},"{self.geneA}","{self.geneB}",{self.partner})'
