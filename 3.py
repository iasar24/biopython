from Bio import SeqIO

# Convert GenBank to FASTA
input_file = "/Users/earth/Downloads/College Materials/pgm/biopython/example.gb"  # Replace with your GenBank file path
output_file = "output.fasta"

SeqIO.convert(input_file, "genbank", output_file, "fasta")
print(f"Converted {input_file} to {output_file}")