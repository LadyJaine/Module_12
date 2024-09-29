import runner_and_tournament
import unittest

class TournamentTest(unittest.TestCase):
    is_frozen = True


    @classmethod
    def setUpClass(cls):
        cls.all_results = {}


    def setUp(self): #setUp - метод, где создаются 3 объекта:
                        # Бегун по имени Усэйн, со скоростью 10.
                        # Бегун по имени Андрей, со скоростью 9.
                        # Бегун по имени Ник, со скоростью 3.
        self.a = runner_and_tournament.Runner("Husein",10)
        self.b = runner_and_tournament.Runner("Andrei",9)
        self.c = runner_and_tournament.Runner("Nick",3)
    @classmethod
    def tearDownClass(cls):
        result = {}
        for key, value in cls.all_results.items():
            print(value)


    # @unittest.skipIf(True, "Тесты в этом кейсе заморожены")

    def test_race_1(self):
        race1 = runner_and_tournament.Tournament(90, self.a, self.c)
        self.res = race1.start()
        loser = list(self.res.values())
        self.assertTrue(loser[-1] == 'Nick')
        # TournamentTest.all_results[1] = res
        TournamentTest.all_results[1] = self.res
    @unittest.skipIf(True, "Тесты в этом кейсе заморожены")
    def test_race_2(self):
        race2 = runner_and_tournament.Tournament(90, self.b, self.c)
        res = race2.start()
        loser = list(res.values())
        self.assertTrue(loser[-1] == 'Nick')
        TournamentTest.all_results[2] = res

    @unittest.skipIf(True, "Тесты в этом кейсе заморожены")

    def test_race_3(self):
        race3 = runner_and_tournament.Tournament(90, self.a,self.b, self.c)
        res = race3.start()
        loser = list(res.values())
        self.assertTrue(loser[-1] == 'Nick')
        self.all_results[3] = res

if __name__ == '__main__':
    unittest.main()

