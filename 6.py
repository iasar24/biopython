from Bio import pairwise2
from Bio.pairwise2 import format_alignment

# Sequences
seq1 = "ATCGTAC"
seq2 = "ATGTTAC"

# Perform pairwise alignment
alignments = pairwise2.align.globalxx(seq1, seq2)

# Display alignments
for alignment in alignments:
    print(format_alignment(*alignment))
