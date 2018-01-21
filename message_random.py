import random_choice
from collections import Counter


class MessageRandom(object):
    def __init__(self):
        pass

    def init_list(self, probabilities_message):
        """
        Initialize list base one weight message list.
        It will return integer list base on index of weight message list.
        """
        if 1 <= len(probabilities_message) <= 1000:
            _list = list()
            for i in range(len(probabilities_message)):
                _list.append(i + 1)
            return _list
        else:
            raise ValueError('Value mus between 1 to 1000')

    def run_random(self, list_messages, probabilitites_message):
        """
        Function pick randomly a message by using weighted_choice function.
        """
        _random = random_choice.RandomChoice.weighted_choice(
            list_messages,
            probabilitites_message)
        return _random

    def weighted(self, probabilities_message):
        """
        Calculate weight of message. Weight of message / Sum(Weight of message).
        """
        if 1 <= len(probabilities_message) <= 1000:
            _weighted = []
            for idx, x in enumerate(probabilities_message):
                if isinstance(x, int):
                    _weighted.append(x / sum(probabilities_message))
                else:
                    raise TypeError('Weight must be Integer')
            return _weighted
        else:
            raise ValueError('Value must between 1 to 1000')


if __name__ == "__main__":
    messageRandom = MessageRandom()
    MESSAGE = [50, 30, 60]
    FACES_OF_DIE = messageRandom.init_list(MESSAGE)
    WEIGHTS = messageRandom.weighted(MESSAGE)
    print(WEIGHTS)
    outcomes = []
    n = 10000
    for _ in range(n):
        outcomes.append(messageRandom.run_random(FACES_OF_DIE, WEIGHTS))
        c = Counter(outcomes)

    for key in c:
        c[key] = c[key] / n

    print(len(outcomes))
    print(sorted(c.items()))
