# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 23:36:01 2019

@author: grant

A function to compute the gc percentage of a dna sequence

Input: dna sequence
Output: gc percentage

"""

def gc(dna):
    "this function computes the gc percentage of a dna sequence"
    nbases=dna.count('n')+dna.count('N')
    gcpercent=float(dna.count('c')+dna.count('C')+dna.count('g')+dna.count('G'))*100.0/(len(dna)-nbases)
    return gcpercent

#gc('AAAGTNNAGTCC'), enter in ipython window after running file, computes 40.0
#help(gc) in ipython window returns the quoted text inside the function
#if you try to print(nbases) in ipython window it fails, local variable only, not global