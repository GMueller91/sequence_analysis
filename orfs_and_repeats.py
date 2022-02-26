# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 13:54:57 2020

@author: grant

Running in Spyder on Anaconda platform 
"""

from Bio import SeqIO
records = SeqIO.parse('dna2.fasta', 'fasta')

orfs = []

#Adjusts frame from biological frame to python index (0,1,2)
def find_orf_frame2(seq):
    frame = 2
    length = 3 * ((len(seq)-frame) // 3)
    for pro in seq[frame:frame+length].translate(table = 1).split("*")[:-1]:
        if 'M' in pro:
            orf = pro[pro.find('M'):]
            orfs.append(orf)

#input biological frame (1,2, or 3)
for record in records:
    find_orf_frame2(record.seq)

max_length = 0
for orf in orfs:   
    if len(orf) > max_length:
        max_length = len(orf)
print("Longest orf in reading frame 2 is: %s" % str(max_length*3+3))