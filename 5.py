from Bio import Entrez

# Set email for Entrez
Entrez.email = "pallavisharma@example.com"  # Replace with your email

# Fetch BRCA1 gene sequence
handle = Entrez.efetch(db="nucleotide", id="NM_007294", rettype="fasta", retmode="text")
fasta_data = handle.read()
handle.close()

# Save or print the result
print(fasta_data)
