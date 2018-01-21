import unittest
from collections import Counter
import math
import operator
import random_queue


class MessageRandomTest(unittest.TestCase):
    def setUp(self):
        self.message_random = random_queue.RandomQueue([50, 30, 60])

    def test_length_init_func(self):
        self.assertEqual(len(self.message_random.list_messages), 3)

    def test_init_func_only_accept_from_0_to_1000(self):
        with self.assertRaises(ValueError):
            random_queue.RandomQueue([])

        with self.assertRaises(ValueError):
            random_queue.RandomQueue([1] * 1001)

    def test_weighted_calculatetion(self):
        self.assertEqual(random_queue.RandomQueue([20, 10, 30]).ratio_weights, [0.3333333333333333, 0.16666666666666666, 0.5])

    def test_weighted_func_only_accept_from_0_to_1000(self):
        with self.assertRaises(ValueError):
            _ratio_weights = random_queue.RandomQueue([]).ratio_weights

        with self.assertRaises(ValueError):
            _ratio_weights = random_queue.RandomQueue([1] * 1001).ratio_weights

    def test_weighted_func_only_accept_integer_value(self):
        with self.assertRaises(TypeError):
            _list_messages = random_queue.RandomQueue([0.1, 20, 30]).list_messages

    def test_probability_output_should_around_probability_input(self):
        _random_queue = self.message_random
        _outcomes = []
        n = 10000
        for _ in range(n):
            _outcomes.append(_random_queue.next())
            c = Counter(_outcomes)

        for key in c:
            c[key] = c[key] / n

        probabiliti_outcome = dict(c)
        for index, i in enumerate(_random_queue.ratio_weights):
            if operator.eq(i, 0):
                self.assertIsNone(probabiliti_outcome.get(index + 1))
            else:
                self.assertTrue(math.isclose(i, probabiliti_outcome.get(index + 1), rel_tol=0.7))


if __name__ == "__main__":
    unittest.main()
