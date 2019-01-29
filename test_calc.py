# the naming convention says that this file should be named test_file.py
# where "file" is the file to be tested
import unittest
import calc  # the file to be tested

class Testcalc(unittest.TestCase):   # this class' name can be anything

	def test_add(self):    # method's name should begin with "test_"
		self.assertEqual(calc.add(10,5),15)
		self.assertEqual(calc.add(10,-4),6)
		self.assertEqual(calc.add(-10,-5),-15)
		self.assertEqual(calc.add(0,5),5)
		
	def test_subtract(self):             # method's name after "test_" can be anything
		self.assertEqual(calc.sub(4,2),2)
		self.assertEqual(calc.sub(-4,-2),-2)
		self.assertEqual(calc.sub(4,-2),6)
		self.assertEqual(calc.sub(4,2),0)  # this test should fail
		
	def test_mul(self):
		self.assertEqual(calc.mul(9,4),36)
		self.assertEqual(calc.mul(9,0),0)
		self.assertEqual(calc.mul(-5,4),-20)
		self.assertEqual(calc.mul(-3,-4),12)

	def test_div(self):
		self.assertEqual(calc.div(9,4),2.25)
		self.assertEqual(calc.div(9,0),0)  # this will throw an error
		self.assertEqual(calc.div(-5,4),-1.25)
		self.assertEqual(calc.div(-3,-4),0.75)
		# two ways for errors raised in the original file
		self.assertRaises(ValueError,calc.mul,10,0) # 1
		with self.assertRaises(ValueError):         # 2
			calc.div(10,0)

if __name__=='__main__':
	unittest.main() # this is included to help us run the code normally or else we will have to run it by adding "-m unittest" before this file's name in the terminal
	
