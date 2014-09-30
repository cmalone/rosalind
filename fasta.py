class FastaRecord:

	def __init__(self, id, dna):
		self.id = id
		self.dna = dna

class FastaReader:

	def __init__(self, record_filename):
		self.records = self.__read_fasta(record_filename)

	def __read_fasta(self, filename):
		"""Reads a file and returns an array of (id, dna) tuples"""
		records = []
		f = open(filename, 'r')

		current_id = ""
		current_dna = ""
		for line in f:
			if line.startswith(">"):
				records.append(FastaRecord(self.__strip(current_id), self.__strip(current_dna)))
				current_id = line[1:]
				current_dna = ""
			else:
				current_dna += line
		records.append(FastaRecord(self.__strip(current_id), self.__strip(current_dna)))
		return records[1:]

	def __strip(self, s):
		return s.lstrip().rstrip().replace("\n", "")
