# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 22:43:17 2020

@author: grant

Using BioPython to interface with NCBI for nucleotide sequence analysis
"""

import Bio

print(Bio.__version__)

from Bio.Blast import NCBIWWW

fasta_string = open("myseq1.fa").read()

result_handle = NCBIWWW.qblast("blastn", "nt", fasta_string)
#blastn program to use, nt database to search against
#for help enter help(NCBIWWW.qblast)

from Bio.Blast import NCBIXML

blast_record = NCBIXML.read(result_handle)

len(blast_record.alignments)

E_VALUE_THRESH = 0.01
for alignment in blast_record.alignments:
	for hsp in alignment.hsps:
		if hsp.expect < E_VALUE_THRESH:
			print('****Alignment****')
			print('sequence:', alignment.title)
			print('length:', alignment.length)
			print('e value:', hsp.expect)
			print(hsp.query)
			print(hsp.match)
			print(hsp.sbjct)