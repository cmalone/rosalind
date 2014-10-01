import fasta

def gc_content(s):
	"""Identify the GC-content of a DNA string (the percentage of the symbols G and C)"""
	c_count = s.count("C")
	g_count = s.count("G")
	gc_percent = 0
	if len(s) > 0:
		gc_percent = float(c_count + g_count) / len(s)
	return gc_percent * 100

def find_highest_gc_content(filename):
	"""Given a file containing DNA strings in FASTA format, return the id and GC content of the string with highest GC content"""
	records = fasta.FastaReader.fromfilename(filename).records
	max_content = 0
	max_content_id = None
	for record in records:
		gc = gc_content(record.dna)
		if gc > max_content:
			max_content = gc
			max_content_id = record.id
	print max_content_id, max_content

find_highest_gc_content("C:\\Users\\cianm\\Downloads\\rosalind_gc (1).txt")