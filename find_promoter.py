#!/usr/bin/env python3
#Use this script for ngs analysis - Grant Mueller 10Nov21
#-+----------------------------------------------------------------------------------------------------------------+-

#Use the Python random module to generate a randomized sequence of 250 million bases: [atcg] , then find promoter.
import random
bases = ['a', 't', 'c', 'g']
sequenceList = []
for n in range(0, 250000000):
    sequenceList.append(random.choice(bases))
chromosome = ‘’.join(sequenceList)

#Search the randomly generated chromosome for a specified promoter sequence using regex and measure the run time.
import time, re
promoter = 'ttgaca.{15, 25}tataat' 
t1 = time.time() 
result = re.finditer(promoter, chromosome) 
t2 = time.time() 
print 'Search time was', (t2-t1), 'seconds'

#--------------------------------------------------------------------------------------------------------------------
#Expected output: Search time was 0.00100994110107 seconds

#Use match objects. 
nmatches = 0 
for match in result:
     nmatches += 1     
     print match.start(), match.end(), match.group() 
print 'Number of search hits = ', nmatches

#Expected output shown below --> ------------------------------------------------------------------------------------
#And when we include this additional code, we get this ...
#
#1199566 1199603 ttgacactcacatcatcagagccccacatagtataat
#2103278 2103308 ttgacacacacagggtttgtgatttataat
#3702112 3702141 ttgacactctttcaaaccaggactataat
# … 
# …
#245627316 245627350 ttgacaaggtctccgtggccccggctattataat
#246256184 246256220 ttgacaggattcctctcgttaattacatcgtataat
#248653641 248653674 ttgacaaccgggctcgtaacgtattagtataat
#Number of search hits =  185

#--------------------------------------------------------------------------------------------------------------------
#Link to source code and article. 
import requests as rq
r = rq.get('https://www.digitalbiologist.com/blog/2018/07/python-for-genomics-and-next-generation-sequencing.html')
try(open(r))

#-+----------------------------------------------------------------------------------------------------------------+-
