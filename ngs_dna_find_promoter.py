#!/usr/bin/env python3
# Grant Mueller - 14Feb22 --------------------------------------------------------------------------+-
# Use this script to generate a random chromosome of 250 million bases and search for a promoter
# --------------------------------------------------------------------------------------------------+-

#Use the Python random module to generate a randomized sequence of 250 million bases a,t,c,g.
import random
bases = ['a', 't', 'c', 'g']
sequenceList = []
for n in range(0, 250000000):
    sequenceList.append(random.choice(bases))
chromosome = "".join(sequenceList)

print("Generated artificial chromosome of length: " + str(len(chromosome)) +
      " bases!\n\nFirst and last three codons:\n" + chromosome[:9] + " ... " + chromosome[-9:])

print("\nSearching for promoters with the structure:\n" +
      "   <-- upstream                                                         downstream -->   \n" +
      "5'-****TTGACA*************************TATAAT****GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG****-3'\n" +
      "        -35                            -10          Gene to be transcribed\n")

# Use regex to search the randomly generated chromosome for a promoter sequence and measure the time. 
import time, re
promoter = 'ttgaca.{15,25}tataat' 
t1 = time.time() 
result = re.finditer(promoter, chromosome) 
t2 = time.time() 
print("Search time was ", (t2-t1), " seconds\n")

# Use match objects to return the start, end, and sequence for each identified promoter.
nmatches = 0 
for match in result:
     nmatches += 1     
     print(match.start(), match.end(), match.group())
print("\nNumber of search hits = ", nmatches)

# --------------------------------------------------------------------------------------------------+-
'''Expected output shown below:
134977 135014 ttgacagagagatagggttggtgcgggaccttataat
1595924 1595959 ttgacattaacgttaaccctctgttgacctataat
2125530 2125566 ttgacacccgcaaaaaagcgtgcttcgagctataat
...
246078993 246079023 ttgacacctcaactttgaaacgagtataat
247451725 247451760 ttgacatacagttctgtccacataaaaattataat
247637482 247637515 ttgacagattcagggccaggaaccagctataat
Number of search hits =  176'''
