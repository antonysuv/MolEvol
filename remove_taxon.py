from Bio import SeqIO


def main():
    parser = argparse.ArgumentParser(description='remove sequence from MSA fasta')
    parser.add_argument( '--in', help = "input file in fasta",dest='FASTA')
    parser.add_argument( '--ta', help = "taxon name to remove",dest='TAXON')
  
    
    args = parser.parse_args()
    
    print("Reading input")
    test_data = np.load(args.TEST)


sequences = SeqIO.parse(args.FASTA, 'fasta')
filtered = [seq for seq in sequences if args.TAXON not in seq.id]

with open(args.FASTA, 'wt') as output:
    SeqIO.write(filtered, output, 'fasta')

if __name__ == "__main__":
    main()
