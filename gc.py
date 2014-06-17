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
	f = open(filename, 'r')
	lines = f.readlines()

	highest_content = 0
	highest_content_id = ""

	current_content = 0
	current_string = ""
	current_id = ""
	for i in range(0, len(lines)):
		if lines[i].startswith(">"):
			last_content = gc_content(current_string)
			if last_content > highest_content:
				highest_content = last_content
				highest_content_id = current_id
			else:
				current_id = lines[i].strip(">")
			current_string = ""
		else:
			current_string = current_string + lines[i].replace("\n", "")
	last_content = gc_content(current_string)
	if last_content > highest_content:
		highest_content = last_content
		highest_content_id = current_id
	print highest_content_id
	print highest_content

# find_highest_gc_content("C:\\Users\\cianm\\Documents\\SublimeProjects\\Rosalind\\test_gc.txt")
			
find_highest_gc_content("C:\\Users\\cianm\\Downloads\\rosalind_gc (1).txt")
