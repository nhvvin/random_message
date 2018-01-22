import math
import random_queue


class TestUtils(object):
    @staticmethod
    def is_close(num_a, num_b, tolerance=0.1):
        return math.isclose(num_a, num_b, rel_tol=tolerance, abs_tol=0.01)

    @staticmethod
    def simulate_random_queue(weight_list):
        _random_queue = random_queue.RandomQueue(weight_list)
        _outcomes = [0] * len(_random_queue.list_messages)
        n = 10000
        for i in range(n):
            _out = _random_queue.next()
            _outcomes[_out - 1] += 1

        _ratio_weight_outcome = _random_queue.calc_ratio_weighted(_outcomes)
        _random_queue
        return _ratio_weight_outcome
