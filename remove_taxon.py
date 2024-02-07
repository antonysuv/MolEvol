from Bio import SeqIO
import sys, argparse, os

def main():
    parser = argparse.ArgumentParser(description='remove sequence from MSA fasta')
    parser.add_argument( '--in', help = "input file in fasta",dest='FASTA')
    parser.add_argument( '--ta', help = "taxon name to remove",dest='TAXON')
  
    
    args = parser.parse_args()
    sequences = SeqIO.parse(args.FASTA, 'fasta')
    filtered = [seq for seq in sequences if args.TAXON not in seq.id]

    with open(args.FASTA, 'wt') as output:
        SeqIO.write(filtered, output, 'fasta')
    print(f"\nRemoved {args.TAXON} from {args.FASTA}")
if __name__ == "__main__":
    main()
