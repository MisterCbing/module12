import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    __repr__ = __str__

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.husein = Runner('Усейн', 10)
        self.andrew = Runner('Андрей', 9)
        self.nik = Runner('Ник', 3)


    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            print(result)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_t1(self):
        results = Tournament(90, self.husein, self.nik).start()
        self.assertEqual(results[2], 'Ник')
        self.all_results.append(results)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_t2(self):
        results = Tournament(90, self.andrew, self.nik).start()
        self.assertEqual(results[2], 'Ник')
        self.all_results.append(results)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_t3(self):
        results = Tournament(90, self.husein, self.andrew, self.nik).start()
        self.assertEqual(results[3], 'Ник')
        self.all_results.append(results)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_t4(self):
        results = Tournament(90, self.andrew, self.husein).start()
        self.assertEqual(results[1], 'Усейн')
        self.all_results.append(results)


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        joe = Runner('Joe')
        for _ in range(10):
            joe.walk()
        self.assertEqual(joe.distance, 50)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        chandler = Runner('Chandler')
        for _ in range(10):
            chandler.run()
        self.assertEqual(chandler.distance, 100)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        rachel = Runner('Rachel')
        monica = Runner('Monica')
        for _ in range(10):
            rachel.walk()
            monica.run()
        self.assertNotEqual(rachel.distance, monica.distance)