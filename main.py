import random


class Combinator:
    def __init__(self):
        self.seq = self.__handle_seq('abcdefghigklmnopqrstuvwxyz')

    def __handle_seq(self, seq):
        return list(seq)

    def get_combinations(self, number=1, max_length=1, min_length=2):
        result = list([None])*number
        for i in range(number):
            item = random.sample(self.seq, random.randint(min_length,
                                 max_length))
            result[i] = ''.join(item)
        return result


if __name__ == '__main__':
    com = Combinator()
    print(print(com.get_combinations(5, 6)))
