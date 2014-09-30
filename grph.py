"""Solution for Overlap Graphs problem -- Currently doesn't work"""
import fasta

def overlaps(s, t, k):
	"""Determines whether or not the length k suffix of s matches the length k prefix of t"""
	suffix = s[len(s) - k: len(s)]
	prefix = t[0:k]
	return suffix == prefix

def computeOverlap(filename, overlap_length):
	records = fasta.FastaReader(filename).records
	for r in records:
		for r2 in records:
			if r.id != r2.id and overlaps(r.dna, r2.dna, overlap_length):
				print r.id, r2.id

computeOverlap(".\\grph_test.txt", 3)