#!/usr/bin/env python3
# Parse a fasta file (.fna) for info and sequence.

def info(f):
    # print the first line of the fasta file
    with open(f) as entry:
        for line in entry:
            if line.startswith('>'):
                print("Reading from file {}:\n{}".format(f, line))


def sequence(f):
    # print the sequence of the fasta file
    from Bio.Seq import Seq
    from Bio import SeqIO

    with open(f) as handle:
        for record in SeqIO.parse(handle, "fasta"):
            print(record.seq)


if __name__ == "__main__":
    import sys
    info(sys.argv[1])
    sequence(sys.argv[1])
    
# ---------------------------------------------------------------------
# call it like this:
# $ python3 read_fasta.py covid.fna
