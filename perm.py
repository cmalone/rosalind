import itertools
import math

def perm(n):
	"""Given n <= 7, prints the number of permutations followed by each permutation"""
	values = range(1, n + 1)
	count = math.factorial(n)
	print count
	for p in itertools.permutations(values):
		current_perm = ""
		for i in p:
			current_perm += " " + str(i)
		print current_perm.lstrip().rstrip()

perm(5)
