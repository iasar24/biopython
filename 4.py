from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

# Create SeqRecord
sequence = Seq("ATGCGAATTCGTA")
seq_record = SeqRecord(
    seq=sequence,  # Use `seq` keyword for the sequence
    id="12345",  # ID is mandatory
    name="ar",  # Optional parameter
    description="Example DNA sequence",  # Optional parameter
    annotations={"molecule_type": "DNA"}  # Optional parameter
)

print(seq_record)
