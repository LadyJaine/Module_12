import unittest
import runner_and_tournament
import tests_12_1
import tests_12_2

races = unittest.TestSuite()


races.addTest(unittest.makeSuite(tests_12_2.TournamentTest))
races.addTest(unittest.makeSuite(tests_12_1.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(races)

