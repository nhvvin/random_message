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

    def test_ratio_weight_output_should_around_ratio_weight_input(self):
        _random_queue = self.message_random
        _outcomes = [0] * len(_random_queue.list_messages)
        n = 10000
        for i in range(n):
            _out = _random_queue.next()
            _outcomes[_out - 1] += 1

        _ratio_weight_outcome = _random_queue.weighted(_outcomes)
        for index, i in enumerate(_random_queue.ratio_weights):
            self.assertTrue(math.isclose(i, _ratio_weight_outcome[index], rel_tol=0.1, abs_tol=0.01))

    def test_output_for_0_ratio(self):
        _random_queue = random_queue.RandomQueue([70, 0, 90])
        _outcomes = [0] * len(_random_queue.list_messages)
        n = 10000
        for i in range(n):
            _out = _random_queue.next()
            _outcomes[_out - 1] += 1

        _ratio_weight_outcome = _random_queue.weighted(_outcomes)
        for index, i in enumerate(_random_queue.ratio_weights):
            self.assertTrue(math.isclose(i, _ratio_weight_outcome[index], rel_tol=0.1, abs_tol=0.01))


if __name__ == "__main__":
    unittest.main()
