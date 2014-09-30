import fasta

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
	for i in range(0, len(records[0].dna)):
		profile_counts["A"].append(0)
		profile_counts["C"].append(0)
		profile_counts["G"].append(0)
		profile_counts["T"].append(0)

	for i in range(0, len(records[0].dna)):
		for j in range(0, len(records)):
			profile_counts[records[j].dna[i]][i] += 1

	return profile_counts

profile = build_profile(fasta.FastaReader("test_profile.txt").records)
print consensus(profile)
for j in range(0, len(profile.items())):
	print profile.items()[j][0] + ": " + str(profile.items()[j][1]).replace("[", "").replace(",", "").replace("]", "")