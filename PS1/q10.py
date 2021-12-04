#Find and fix all errors (both syntax/logical) in the following code which will print the sequence “1 3 5 7 9 11 13 15 17 19”:


class Progression:
	def __init__(start=0):
		self._current = start

	def _advance(self):
		self._current += 1

	def __next__(self):
		if self._current is None:
			raise Stopiteration()
		else:
			answer = self._current
			self._advance()
			return answer

	def __iter__(self):
		return self


class ArithmeticProgression extends Progression

	def init(self, increment=1, start=0):
		super().__init__(start)
		self._increment = increment


	def advance(self):
		self._increment += self._current


if __name__ == "__main__":
	a = ArithmeticProgression(2, 1)
print(" ".join(str(next(a)) for _ in range(10)))