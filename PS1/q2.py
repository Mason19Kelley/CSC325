''' Write a Python class named "AbsoluteProgression" that extends the Progression class
so that each value in the progression is the absolute value of the difference between the previous two values.
You should include a constructor that accepts a pair of numbers as the first two values, using 2 and 200 as the defaults.
Assume that the first number in the progression is the absolute difference of the first two values (198 with the defaults). '''
class Progression:
    def __init__(self, start=0):
        self._current = start
    def _advance(self):
        self._current += 1
    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer
    
    def __iter__(self):
        return self
    
    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))

class AbsoluteProgression(Progression):
    def __init__(self, num1 = 2, num2 = 200):
        Progression.__init__(abs(num1-num2))
        self.num1 = num1
        self.num2 = num2 # since first in progression is |200-2|, or 198, this will be the previous value in the progression

    def advance(self):

if __name__ == "__main__":
    AbsoluteProgression().print_progression(20)
