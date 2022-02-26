# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 16:43:54 2020

@author: grant
"""

seq=input("Please enter a dna sequence: ")

def reversecomplement(seq) :
	""" Return the reverse complement of the dna string."""
	seq = reverse_string(seq)
	seq = complement(seq)
	return seq

#add reverse_string fx
def reverse_string(seq):
	return seq[::-1]

#add complement fx
def complement(dna):
	"""Return the complementary sequence string."""
	basecomplement = {'A':'T', 'C':'G', 'G':'C', 'T':'A', 'N':'N', 'a':'t', 'c':'g', 'g':'c', 't':'a', 'n':'n'}
	letters = list(dna)
	letters = [basecomplement[base] for base in letters]
	return ''.join(letters)

#syntax eg: new_list = [operation(i) for i in old_list if filter(i)]
#operation and filter will be defined
    
print("The reverse complement is:   %s" % reversecomplement(seq))

#eg input: 'atgtag' returns: 'ctacat'
    
"""Calling a variable number of arguments:

def newfunction(first, second, third, *therest):
	print("First: %s" % first)
	print("Second: %s" % second)
	print("Third: %s" % third)
	print("And all the rest... " therest)
	return

call: newfunction(1,2,3,4,5), will return the arguments in order (1,2,3,4&5)"""
	