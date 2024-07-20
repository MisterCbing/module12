import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        joe = Runner('Joe')
        for _ in range(10):
            joe.walk()
        self.assertEqual(joe.distance, 50)

    def test_run(self):
        chandler = Runner('Chandler')
        for _ in range(10):
            chandler.run()
        self.assertEqual(chandler.distance, 100)

    def test_challenge(self):
        rachel = Runner('Rachel')
        monica = Runner('Monica')
        for _ in range(10):
            rachel.walk()
            monica.run()
        self.assertNotEqual(rachel.distance, monica.distance)