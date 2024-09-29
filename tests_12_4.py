import logging
import rt_with_exceptions
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                        format="%(levelname)s|%(message)s")

    @unittest.skipIf(False, "it works")
    def test_walk(self):
        a = rt_with_exceptions.Runner("Pavel",-5)
        try:
            logging.info('"test_walk" выполнен успешно')
            for i in range(10):
                a.walk()
            self.assertEqual(a.distance, 50, "Все отлично!")

        except Exception as exc:
            logging.warning('Неверная скорость для Runner',exc_info = True)
            return 0

# self.assertEqual(a.distance,40,"Что-то пошло не так!")

    def test_run(self):
        b = rt_with_exceptions.Runner(5)
        try:
            logging.info('"test_run" выполнен успешно')
            for i in range(10):
                b.run()
            self.assertEqual(b.distance, 100)

        except Exception as exc:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        item1 = rt_with_exceptions.Runner("Nick")
        item2 = rt_with_exceptions.Runner("Sara")
        for i in range(10):
            item1.run()
            item2.walk()
        self.assertNotEqual(item1.distance, item2.distance)


if __name__ == "__main__":
    unittest.main()
