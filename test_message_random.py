import unittest
import message_random
from collections import Counter
import math
import operator


class MessageRandomTest(unittest.TestCase):
    def setUp(self):
        self.messageRandom = message_random.MessageRandom()

    def test_length_init_func(self):
        self.assertEqual(len(self.messageRandom.init_list([10, 20, 30])), 3)

    def test_init_func_only_accept_from_0_to_1000(self):
        with self.assertRaises(ValueError):
            self.messageRandom.init_list([])

        with self.assertRaises(ValueError):
            self.messageRandom.init_list([1] * 1001)

    def test_weighted_calculatetion(self):
        self.assertEqual(self.messageRandom.weighted([20, 10, 30]), [0.3333333333333333, 0.16666666666666666, 0.5])

    def test_weighted_func_only_accept_from_0_to_1000(self):
        with self.assertRaises(ValueError):
            self.messageRandom.weighted([])

        with self.assertRaises(ValueError):
            self.messageRandom.weighted([1] * 1001)

    def test_weighted_func_only_accept_integer_value(self):
        with self.assertRaises(TypeError):
            self.messageRandom.weighted([0.1, 20, 30])

    def test_probability_output_should_around_probability_input(self):
        _message = [50, 30, 60]
        _faces_of_die = self.messageRandom.init_list(_message)
        _weights = self.messageRandom.weighted(_message)
        _outcomes = []
        n = 10000
        for _ in range(n):
            _outcomes.append(self.messageRandom.run_random(_faces_of_die, _weights))
            c = Counter(_outcomes)

        for key in c:
            c[key] = c[key] / n

        probabiliti_outcome = dict(c)
        for index, i in enumerate(_weights):
            if operator.eq(i, 0):
                self.assertIsNone(probabiliti_outcome.get(index + 1))
            else:
                self.assertTrue(math.isclose(i, probabiliti_outcome.get(index + 1), rel_tol=0.7))


if __name__ == "__main__":
    unittest.main()
