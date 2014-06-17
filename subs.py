import time

def find_motif(s, t):
	"""Given strings s, t where t is a substring of s, return all 1-based indices of instances of t in s"""
	matches = []
	for i in range(0, len(s) - len(t)):
		if s[i : i + len(t)] == t:
			matches.append(i + 1) # 1-indexed
	return matches

def find_motif_rabin_karp(s, t):
	"""Implements find_motif using the Rabin-Karp string search algorithm
	   (O(m + n) avg and best case run time, but still O(m*n) worst-case)"""
	matches = []
	ht = hash_rabin_karp(t)
	hs = hash_rabin_karp(s[0:len(t)])
	for i in range(0, len(s) - len(t)):
		if hs == ht:
			if s[i:i + len(t)] == t:
				matches.append(i + 1) # 1-indexed
		hs = hash_rabin_karp(s[i + 1 : i + len(t) + 1])
	return matches

def hash_rabin_karp(s):
	"""Hash for Rabin-Karp algorithm -- not a rolling hash"""
	hash_value = 0
	hash_base = 101
	for i in range(0, len(s)):
		hash_value += ord(s[i]) * hash_base**(len(s) - i - 1)
	return hash_value

def find_motif_knuth_morris_pratt(s, t):
	"""Implements find_motif using the Knuth-Morris-Pratt algorithm
	   (O(m + n) worst-case performance)"""
	return []

def find_motif_boyer_moore(s, t):
	"""Implements find_motif using the Boyer-Moore algorithm with Galil rule
	   (O(m + n) worst-case performance)"""
	return []

def find_motif_aho_corasick(s, t):
	"""Implements find_motif using the Aho-Corasick
	   (O(m + n) worst-case performance)"""
	return []

def run_algo(s, t, f):
	motif_locations = ""
	start = time.time()
	locations = f(s, t)
	for i in locations:
		motif_locations += str(i) + " "
	end = time.time()
	print "algo: " + str(f.__name__)
	print "duration: " + str(end - start)
	print motif_locations + "\n"

s = "CAGTTGCGCAGTTGCCCAGTTGCACAGTTGCCAGTTGCCAGTTGCCAGTTGCAACCAGTTGCACAGTTGCTCCAGTTGCATCCACACTCCAGTTGCATGCCCAGTTGCACAGTTGCATCAGTTGCTCCAGTTGCTCAGTTGCAAGCAGTTGCCAGTTGCCAGTTGCGCAGTTGCCGATTCACCAGTTGCCAGTTGCTCCAGTTGCTCAGTTGCTTCGCAGTTGCCAGTTGCACAGTTGCGCAGTTGCACAGTTGCAAGAATTCAGTTGCATCCAGTTGCCAGTTGCATCCAGTTGCCAGTTGCGCAGTTGCCAGTTGCCAGTTGCCGACTAGGAGCAGTTGCGTTCACTCCAGTTGCTGACAATACAGTTGCCGTGCAGTTGCGGCCAGTTGCCAGAGGTCAGTTGCTCAGTTGCCAGTTGCGTTTAGCAGTTGCGGGTAACAGTTGCGAACTCTTTAGCCGATTCCAGTTGCATTCAGTTGCCCAGTTGCTTCCAGTTGCTGTACAGTTGCGGCCCAAACCCCAGTTGCCAGTTGCCAGTTGCCAGTTGCCGCTAGCAGTTGCCAGTTGCTCAGCAGTTGCTCCAGTTGCCAGTTGCCCCAGTTGCTCGGACAGTTGCACCGCTCAGTTGCGCGCATACACAGTTGCCCAGCAGTTGCTGCAGTTGCCAGTTGCAGTCATGGCAGTTGCACAGTTGCTACAGTTGCCCAGTTGCGTGAACAGTTGCCAGTTGCCAGTTGCCAGTTGCCAGTTGCTAACTGTTGCCTGGGGCAGTTGCCAGTTGCGTATGGCACAGTTGCGGCTCAGCGTCAGTTGCCGTGCTGACACAGTTGCCTTACAGTTGCCAGTTGCTTTCAGTTGCACCCCGCAGTTGCACCTTCAGTTGCTGCAGTTGCCAGTTGCCAGTTGCCAGTTGCGCAGTTGCAACAGTTGCCAGTTGCAAACCCAGTTGCCAGTTGCCCAGTTGCCAGTTGCTAACGAGAATTGCAGTTGC"
t = "CAGTTGCCA"
run_algo(s, t, find_motif)
run_algo(s, t, find_motif_rabin_karp)