#!/usr/bin/env python3
#Nathaniel Jones
#https://github.com/njj19c/NJbch5884

import sys

#reads the pdb file input
pdb=open("2FA9noend.pdb",'r') 
lines=pdb.readlines()


# Produces lists for input
element_list=[]
element_type=[]
original_a=[]
original_b=[]
original_c=[]
new_a=[]
new_b=[]
new_c=[]
    

#splits the data into xyz components and gives elements as type
for l in lines:
	atom=l.split()
	atom[1]=int(atom[1])
	atom[5]=int(atom[5])
	atom[6]=float(atom[6])
	atom[7]=float(atom[7])
	atom[8]=float(atom[8])
	atom[9]=float(atom[9])
	atom[10]=float(atom[10])
	element_type.append(atom)
    
#produces atom list
element_list.append(atom) 
x=float(atom[6])
y=float(atom[7])
z=float(atom[8])
element_name=atom[11]
original_a.append(x)
original_b.append(y) 
original_c.append(z)
element_type.append(element_name)

#formats for output
pdb_format='{:6s}{:5d} {:^4s}{:1s} {:3s} {:1d} {:8.3f}{:8.3f}{:8.3f}{:6.2f}{:6.2f} {:>2s}\n'

#generate file for writing out
output = open("writeout.pdb","w")
 
for l in element_list:
    output.write(pdb_format.format(*l))
output.close()
print("writeout.pdb successfully written")

sys.exit()