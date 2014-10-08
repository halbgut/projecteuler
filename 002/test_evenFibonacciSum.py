import unittest
from evenFibonacciSum import EvenFibonacciSum

class TestEvenFibonacciSum(unittest.TestCase):
	def setUp(self):
		self.maxval = 100
		self.evenFibonacciSum = EvenFibonacciSum()

	def test_EvenFibonacciSum_calc(self):
		self.assertTrue(type(evenFibonacciSum.calc(self.maxval)) == int)
		self.assertRaises(TypeError, self.evenFibonacciSum.calc, [1,2,3])

	def test_EvenFibonacciSum__getFibonacciTo(self):
		self.assertTrue(type(evenFibonacciSum._getFibonacciTo(self.maxval)) == list)
		lastTwo = ()
		for n in evenFibonacciSum._getFibonacciTo(self.maxval):
			if len(lastTwo == 2):
				self.assertTrue(sum(lastTwo) == n)
				lastTwo[0] = lastTwo[1]
				lastTwo[1] = n
			else:
				lastTwo.append(n)

if __name__ == '__main__':
	unittest.main()