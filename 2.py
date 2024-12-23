from Bio import SeqIO

# Read FASTA file
file_path = "/Users/earth/Downloads/College Materials/pgm/biopython/example.fasta"  # Replace with your FASTA file path
for record in SeqIO.parse(file_path, "fasta"):
    print(f"ID: {record.id}")
    print(f"Sequence: {record.seq}")
