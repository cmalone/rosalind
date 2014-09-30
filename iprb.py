def probability(k, m, n):
	"""Given a population containing k + m + n organisms:
		k are homozygous dominant for a factor,
		m are heterozygous,
		n are homozygous recessive;
		Return the probability that two randomly selected mating
		organisms will produce an individual possessing a dominant allele."""
	population = k + m + n

	p_nondominant_chosen = float(k + m) / population
	p_other_nondominant_chosen = float(k + m - 1) / population
	p_nondominant_result = p_nondominant_chosen * p_other_nondominant_chosen

	return p_nondominant_result

print probability(2, 2, 2)