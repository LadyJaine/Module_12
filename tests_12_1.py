import runner
import unittest

class RunnerTest(unittest.TestCase):

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
        self.assertNotEqual(item1.distance,item2.distance)

if __name__ == "__main__":
    unittest.main()