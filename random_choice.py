import numpy as np


class RandomChoice(object):
    @staticmethod
    def weighted_choice(sequence, weights):
        """
        weighted_choice selects a random element of
        the sequence according to the list of weights
        """
        x = np.random.random()
        cum_weights = [0] + list(np.cumsum(weights))
        index = RandomChoice.find_interval(x, cum_weights)
        return sequence[index - 1]

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
