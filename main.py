import random
from typing import List


class Combinator:
    def __init__(self) -> None:
        self.seq = self.__handle_seq('abcdefghigklmnopqrstuvwxyz')

    def __handle_seq(self,
                     seq: str
                     ) -> List:
        return list(seq)

    def get_combinations(self,
                         number: int = 1,
                         max_length: int = 1,
                         min_length: int = 2
                         ) -> str:
        result = list([None])*number
        for i in range(number):
            item = random.sample(self.seq, random.randint(min_length,
                                 max_length))
            result[i] = ''.join(item)
        return result


if __name__ == '__main__':
    com = Combinator()
    print(print(com.get_combinations(5, 6)))
