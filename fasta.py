class FastaRecord:

	def __init__(self, id, dna):
		self.id = id
		self.dna = dna

class FastaReader:

	def __init__(self, lines):
		"""Initialize from a sequence of FASTA lines"""
		self.records = self.__process_fasta_sequence(lines)

	@classmethod
	def fromfilename(cls, filename):
		lines = []
		f = open(filename, 'r')
		for line in f:
			lines.append(line)
		return cls(lines)

	@classmethod
	def fromlines(cls, lines):
		return cls(lines)

	def __process_fasta_sequence(self, lines):
		"""Reads a file and returns an array of (id, dna) tuples"""
		records = []

		current_id = ""
		current_dna = ""
		for line in lines:
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
