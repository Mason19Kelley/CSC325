#Find and fix all errors (both syntax/logical) in the following code which will print the sequence “1 3 5 7 9 11 13 15 17 19”:

class Progression:
    # def __init__(start = 0): constructor must have self
    def __init__(self, start = 0):
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            # raise Stopiteration() incorrect capitalization -- refer to slide 16 of python primer 2
            raise StopIteration()

        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self


# class ArithmeticProgression extends Progression incorrect form of inheritance in python
class ArithmeticProgression(Progression):
    #def init(self, increment = 1, start = 0): constructor missing __ on both sides of init
    #def __init__(self, increment = 1, start = 0): incremebt by 2 instead of 1 and start at 1
    def __init__(self, increment = 2, start = 1):
        super().__init__(start)
        self._increment = increment


    #def advance(self): from super class, incorrect name of method
    def _advance(self):
        #self._increment += self._current incorrect logic, increment current variable
        self._current += self._increment


if __name__ == "__main__":
    a = ArithmeticProgression(2, 1)
  #print(" ".join(str(next(a)) for _ in range(10))) tab/spacing error in python
    print(" ".join(str(next(a)) for _ in range(10)))