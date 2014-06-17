def rabbits(n, k):
	"""Rabbit population model based on n months and litters size k pairs"""
	rabbit_pairs_count = 1
	// n = 5, k = 3 => 1, 4, 16
	for i in range(1, n):
