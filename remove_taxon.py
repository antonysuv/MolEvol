from Bio import SeqIO

sequences = SeqIO.parse('test.fasta', 'fasta')
filtered = [seq for seq in sequences if 'VRE32514' not in seq.id]

with open('output.fasta', 'wt') as output:
    SeqIO.write(filtered, output, 'fasta')
