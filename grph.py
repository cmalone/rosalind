"""Solution for Overlap Graphs problem -- Currently doesn't work"""
from collections import namedtuple

def overlaps(s, t, k):
	"""Determines whether or not the length k suffix of s matches the length k prefix of t"""
	suffix = s[len(s) - k: len(s)]
	prefix = t[0:k]
	return suffix == prefix

def read_fasta_records(filename):
	"""Reads a file and returns an array of (id, dna) tuples"""
	records = []
	Record = namedtuple("Record", "Id Dna")
	f = open(filename, 'r')

	current_id = ""
	current_dna = ""
	for line in f:
		if line.startswith(">"):
			records.append(Record(strip(current_id), strip(current_dna)))
			current_id = line[1:]
			current_dna = ""
		else:
			current_dna += line
	records.append(Record(strip(current_id), strip(current_dna)))
	return records[1:]

def strip(s):
	return s.lstrip().rstrip()

records = read_fasta_records("test_records.txt")
# Forwards
for i in range(0, len(records) - 1):
	for j in range(i + 1, len(records)):
		if overlaps(records[i].Dna, records[j].Dna, 3):
			print records[i].Id + " " + records[j].Id
# Backwards
for i in range(len(records) - 1, 1, -1):
	for j in range(i - 1, 0, -1):
		if overlaps(records[len(records) - j].Dna, records[len(records) - i].Dna, 3):
			print records[len(records) - j].Id + " " + records[len(records) - i].Id
