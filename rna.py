def solution(s):
	"""Transcribe a DNA string to its corresponding RNA string"""
	rna = s.replace("T", "U")
	return rna

print solution("GAAATGGGCTAAAAACTCTTCCCATACTAGGAGAACATCAGTATCGTTTAGGCGAAAGCCTGTACGTACAAGTACTTTGGCTGGTGTCTCTTGGTCCATCATCTCATCACTCGCCCCTCGGACGAAGGCACAAAAGGTTTCGTACTTTCATCGTGCGCTTAGCGCGGGCGGTGGTTCCGATACAGTAAAGAGCTGCACCCCGAGGAGTCCATCATGAATATTTTACCAATTTCACCTATGAGGTCCTATCTCGGCCCTCCGCCCGGGCGACCCCCCCGTTTATATCTGGTATCGCGTCCCCACGGACTTTATCTCTTCGCGTGACCAAATAAAGTGCTGTTTTTAGCGTTCAGCAGTTTCTAAGCAATACGATGAAGCTAATGCTTTCTTTGTGCAATGATTCAATGCGAGACGCGATATTAGCTTTACGGGCGTGCCGGGACGAATAGTCATAGCTGCCTAACCTCTGGTCCGGACTGACAAAGATGCCATGGTACATCAGTATCTGGAAGCCTTCTATCCGCGATTCGGTACGAGCTGATCTACCCGTGATCCTAGACACTAGACCTTGCGACAAAGTTATTGTCAGCTGCTAGTAAAGGTCTACTTTCAGAATTATTAGCACGTTTGAAAAGCGCCACGAATTACGATGCCCTTCCTCTGGCTGCAGTGCCTCTAAAGTTTGGCGGTTTCTCGGCTTTTGCATACTTCTGCGCGAACCCGGCCCCGAAATCGCACGATCTACCCACACGCAATCTGATGCTTGGCGAGGGCCACACGCTAGGAGCTCTAAGGTTAAGCCCAGCTAGTTCTGTGCTCGCTAGGCCGCAGTGGAGTCGAGAACTGCTACATTTGTTGCCAACTCCCGCGGTGGCTGACGACATAGAGAGGACCAGAGATGGGTTAGGAGCAACAGTTGGTAACAATAAGGTCAGCCGGTC")
