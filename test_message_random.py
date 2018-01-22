import unittest
import random_queue
from test_utils import TestUtils


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
        self.assertEqual(random_queue.RandomQueue(
            [20, 10, 30]).ratio_weights,
            [0.3333333333333333, 0.16666666666666666, 0.5])

    def test_weighted_func_only_accept_from_0_to_1000(self):
        with self.assertRaises(ValueError):
            _ratio_weights = random_queue.RandomQueue([]).ratio_weights

        with self.assertRaises(ValueError):
            _ratio_weights = random_queue.RandomQueue([1] * 1001).ratio_weights

    def test_weighted_func_only_accept_integer_value(self):
        with self.assertRaises(TypeError):
            _list_messages = random_queue.RandomQueue([0.1, 20, 30]).list_messages

    def test_ratio_weight_output_should_around_ratio_weight_input(self):
        _outcomes = TestUtils.simulate_random_queue([50, 30, 60])
        _ratio_weight_outcome = TestUtils.simulate_random_queue([50, 30, 60])

        for index, i in enumerate(random_queue.RandomQueue([50, 30, 60]).ratio_weights):
            self.assertTrue(TestUtils.is_close(i, _ratio_weight_outcome[index]))

    def test_output_for_0_ratio(self):
        _outcomes = TestUtils.simulate_random_queue([70, 0, 90])
        _ratio_weight_outcome = TestUtils.simulate_random_queue([70, 0, 90])

        for index, i in enumerate(random_queue.RandomQueue([70, 0, 90]).ratio_weights):
            self.assertTrue(TestUtils.is_close(i, _ratio_weight_outcome[index]))


if __name__ == "__main__":
    unittest.main()
