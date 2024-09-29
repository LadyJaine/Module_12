import runner
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(False, "it works")
    def test_walk(self):
        a = runner.Runner("Pavel")
        for i in range(10):
            a.walk()
        self.assertEqual(a.distance, 50, "Все отлично!")
        # self.assertEqual(a.distance,40,"Что-то пошло не так!")

    def test_run(self):
        b = runner.Runner("Serg")
        for i in range(10):
            b.run()
        self.assertEqual(b.distance, 100)

    def test_challenge(self):
        item1 = runner.Runner("Nick")
        item2 = runner.Runner("Sara")
        for i in range(10):
            item1.run()
            item2.walk()
        self.assertNotEqual(item1.distance, item2.distance)


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
            for k, v in value.items():
                result[k] = str(v)
            print(result)


    @unittest.skipIf(True, "Тесты в этом кейсе заморожены")

    def test_race_1(self):
        race1 = runner_and_tournament.Tournament(90, self.a, self.c)
        res = race1.start()
        loser = list(res.values())
        self.assertTrue(loser[-1] == 'Nick')
        self.all_results[res.values()] = res
    @unittest.skipIf(True, "Тесты в этом кейсе заморожены")
    def test_race_2(self):
        race2 = runner_and_tournament.Tournament(90, self.b, self.c)
        res = race2.start()
        loser = list(res.values())
        self.assertTrue(loser[-1] == 'Nick')
        self.all_results[res.values()] = res

    @unittest.skipIf(True, "Тесты в этом кейсе заморожены")
    def test_race_3(self):
        race3 = runner_and_tournament.Tournament(90, self.a,self.b, self.c)
        res = race3.start()
        loser = list(res.values())
        self.assertTrue(loser[-1] == 'Nick')
        self.all_results[res.values()] = res

if __name__ == "__main__":
    unittest.main()