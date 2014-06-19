def rabbits(n, k):
	"""Rabbit population model based on n months and litters size k pairs"""
	young_pairs_count = 1
	repro_age_pairs_count = 0

	for i in range(1, n):
		aging_pairs = young_pairs_count
		young_pairs_count = k * repro_age_pairs_count
		repro_age_pairs_count += aging_pairs
	
	return young_pairs_count + repro_age_pairs_count

print rabbits(36, 2)