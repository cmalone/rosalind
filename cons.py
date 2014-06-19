from collections import namedtuple

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
	return s.lstrip().rstrip().replace("\n", "")

def consensus(profile):
	cons_string = ""
	profile_length = len(profile["A"]) # All profile strings should be same length
	for i in range(0, profile_length):
		max_count = max([profile["A"][i], profile["C"][i], profile["G"][i], profile["T"][i]])
		if profile["A"][i] == max_count:
			cons_string += "A"
		elif profile["C"][i] == max_count:
			cons_string += "C"
		elif profile["G"][i] == max_count:
			cons_string += "G"
		elif profile["T"][i] == max_count:
			cons_string += "T"
	return cons_string

def build_profile(records):
	"""Builds a profile matrix from a set of (id, dna) records, where all dna strings are of the same length"""
	profile_counts = {"A": [], "C": [], "G": [], "T":[]}
	for i in range(0, len(records[0].Dna)):
		profile_counts["A"].append(0)
		profile_counts["C"].append(0)
		profile_counts["G"].append(0)
		profile_counts["T"].append(0)

	for i in range(0, len(records[0].Dna)):
		for j in range(0, len(records)):
			profile_counts[records[j].Dna[i]][i] += 1

	return profile_counts

profile = build_profile(read_fasta_records("test_profile.txt"))
print consensus(profile)
for j in range(0, len(profile.items())):
	print profile.items()[j][0] + ": " + str(profile.items()[j][1]).replace("[", "").replace(",", "").replace("]", "")