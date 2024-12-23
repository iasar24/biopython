from Bio.Seq import Seq

dna_seq = Seq("ATGCGAATTCGTA")


subsequence = dna_seq[2:8]
print("Subsequence (3rd to 8th):", subsequence)


amino_acids = dna_seq.translate()
print("Translated sequence:", amino_acids)
