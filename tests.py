from main import main, reproduceGeneration
import unittest

class TestGenesMethods(unittest.TestCase):

    def test_zero_gens(self):
        self.assertEqual(main(0, 100, 0.5, 0.5, 0), -1)

    def test_one_gen(self):
        pops, num_pops = main(1, 100, 0.5, 0.5, 0)
        self.assertEqual(num_pops, 1)

    def test_two_gens(self):
        pops, num_pops = main(2, 100, 0.5, 0.5, 0)
        self.assetEqual(num_pops, 2)

    def test_higher_num_gens(self):
        pops, num_pops = main(20, 100, 0.5, 0.5, 0)
        self.assetEqual(num_pops >  10, True)

    def test_empty_mono_reproduceGeneration(self):
        creatures = []
        gen = reproduceGeneration(creatures, true)
        self.assertEqual(len(gen), 0)

    def test_empty_poly_reproduceGeneration(self):
        creatures = []
        gen = reproduceGeneration(creatures, false)
        self.assertEqual(len(gen), 0)

    def test_one_reproduceGeneration(self):
        creatures = [Creature(1, 'A', 'B')]
        gen = reproduceGeneration(creatures, false)
        self.assertEqual(len(gen), 0)

    def test_nonzero_reproduceGeneration(self):
        creatures = [
            Creature(1, 'A', 'A'),
            Creature(1, 'B', 'B'),
            Creature(1, 'A', 'A'),
            Creature(1, 'B', 'B'),
            Creature(1, 'A', 'A'),
            Creature(1, 'B', 'B'),
            Creature(1, 'A', 'A'),
            Creature(1, 'B', 'B'),
            Creature(1, 'A', 'A'),
            Creature(1, 'B', 'B'),
            Creature(1, 'A', 'A'),
            Creature(1, 'B', 'B'),
            Creature(1, 'A', 'A'),
            Creature(1, 'B', 'B')
        ]
        gen = reproduceGeneration(creatures)
        self.assertEqual(len(gen) > 0, True)

    def test_nonCompatible_monogamy_reproduceGeneration(self):
        creatures = [Creature(1, 'A', 'A', 1), Creature(1, 'B', 'B', 10)]
        gen = reproduceGeneration(creatures)
        self.assertEqual(len(gen), 0)

    def test_nonCompatible_polygamy_repoduceGeneration(self):
        creatures = [
            Creature(1, 'A', 'A', 1),
            Creature(1, 'B', 'B', 10),
            Creature(1, 'A', 'A', 1),
            Creature(1, 'B', 'B', 10),
            Creature(1, 'A', 'A', 1),
            Creature(1, 'B', 'B', 10),
            Creature(1, 'A', 'A', 1),
            Creature(1, 'B', 'B', 10),
            Creature(1, 'A', 'A', 1),
            Creature(1, 'B', 'B', 10),
            Creature(1, 'A', 'A', 1),
            Creature(1, 'B', 'B', 10),
            Creature(1, 'A', 'A', 1),
            Creature(1, 'B', 'B', 10),
            Creature(1, 'A', 'A', 1),
            Creature(1, 'B', 'B', 10),
            Creature(1, 'A', 'A', 1),
            Creature(1, 'B', 'B', 10),
            Creature(1, 'A', 'A', 1),
            Creature(1, 'B', 'B', 10),
            Creature(1, 'A', 'A', 1),
            Creature(1, 'B', 'B', 10),
            Creature(1, 'A', 'A', 1),
            Creature(1, 'B', 'B', 10),
        ]
        gen = reproduceGeneration(creatures, monogamyFlag=false)
        self.assertEqual(len(gen) > 0, True)
        pass
if __name__ == '__main__':
    unittest.main()