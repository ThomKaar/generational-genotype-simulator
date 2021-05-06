from Population import Population, populateGeneration
from Reproduce import Reproduce
from random import randint
from sys import argv

def reproduceGeneration(creatures, monogamyFlag, parthenogenesis=False):
    nextGen = []
    # for each creature in the gen
    #   find a random creature in the gen
    #   if the creature's index is equal it's partner find another creature
    #   (optional) if the creature already has a partner find another creature
    #   else
    #       mark the creatures as partners
    #       have the two creatures reproduce
    #       append reproduced creatures to nextGen
    genSize = len(creatures)
    if genSize == 1 and parthenogenesis == False:
        return nextGen
    for creature in creatures:
        if parthenogenesis:
            reproduction = Reproduce(creature, None, parthenogenesis=parthenogenesis)
        else:
            if monogamyFlag and creature.partner is not None:
                continue
            partnerIndex = randint(0, genSize-1)
            while creatures[partnerIndex].id == creature.id and \
            (not monogamyFlag or creatures[partnerIndex].partner != creature.id):
                partnerIndex = randint(0, genSize-1)
            creatures[partnerIndex].partner = creature.id
            creature.partner = creatures[partnerIndex].id
            reproduction = Reproduce(creature, creatures[partnerIndex])
        nextGen += reproduction.offspring
    return nextGen

def main(number_of_gens=2, init_pop_size=100, percA=0.5, percB=0.5, percMix=0, monogamyFlag=True):
    if number_of_gens <= 0:
        return -1
    gen = populateGeneration(1, init_pop_size, percA, percB, percMix)
    pops = []
    last_pop = None
    gen_num = 1
    while (gen_num <= number_of_gens and (last_pop is None or len(gen) > 1)):
        last_pop = Population(creatures=gen)
        pops.append(last_pop)
        gen = reproduceGeneration(last_pop.creatures, monogamyFlag=monogamyFlag)
        gen_num += 1

    return pops, len(pops)

if __name__== "__main__":
    call_args = [2, 100, 0.5, 0.5, 0, True]
    for i in range(len(argv[1:])):
        call_args[i] = argv[i+1]
    main(int(call_args[0]), int(call_args[1]), float(call_args[2]), float(call_args[3]), float(call_args[4]), bool(call_args[5]))
