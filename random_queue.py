import numpy as np


class RandomQueue(object):
    def __init__(self, weight_list):
        self.list_messages = self.init_list_messages(weight_list)
        self.weight_list = weight_list
        self.ratio_weights = self.weighted(self.weight_list)
        self.acc_ratio_weights = [0] + list(np.cumsum(self.ratio_weights))

    def init_list_messages(self, weight_list):
        """
        Initialize list base one weight message list.
        It will return integer list base on index of weight message list.
        """
        if 1 <= len(weight_list) <= 1000:
            _list = list()
            for i in range(len(weight_list)):
                _list.append(i + 1)
            return _list
        else:
            raise ValueError('Value mus between 1 to 1000')

    def weighted(self, weight_list):
        """
        Calculate weight of message. Weight of message / Sum(Weight of message).
        """
        _sum_weights = sum(weight_list)
        if 1 <= len(weight_list) <= 1000:
            _weighted = []
            for idx, x in enumerate(weight_list):
                if isinstance(x, int):
                    _weighted.append(x / _sum_weights)
                else:
                    raise TypeError('Weight must be Integer')
            return _weighted
        else:
            raise ValueError('Value must between 1 to 1000')

    @staticmethod
    def find_interval(x, partition):
        """
        Find_interval -> i, "i" will be the smallest index
        for which applies x < partition[i]. If no such index exists
        "i" will be set to len(partition)
        """
        for i in range(0, len(partition)):
            if x < partition[i]:
                return i
        return len(partition)

    def next(self):
        """
        """
        x = np.random.random()
        index = self.find_interval(x, self.acc_ratio_weights)
        _random = self.list_messages[index - 1]
        return _random


if __name__ == "__main__":
    random_queue = RandomQueue([50, 30, 60])
    print(random_queue.next())
