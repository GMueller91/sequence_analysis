# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 11:26:43 2020

@author: grant
"""

# define has_stop_codon function here
def has_stop_codon(dna,frame=0) :
	"This function checks if given dna sequence has in frame stop codons."
	stop_codon_found=False
	stop_codons=['tga','tag','taa']
	for i in range(frame,len(dna),3) :
		codon=dna[i:i+3].lower()
		if codon in stop_codons :
			stop_codon_found=True
			break
	return stop_codon_found

dna= input("Enter a DNA sequence, please:")
if(has_stop_codon(dna)):
	print("Input sequence has an in frame stop codon.")
else:
	print("Input sequence has no in frame stop codons.")
    
#Run file, then in ipython console enter has_stop_codon('atag',1), returns True