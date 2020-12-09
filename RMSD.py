#!/usr/bin/env python3
#Nathaniel Jones
# https://github.com/hannahoday/bch5884.git

import sys
import math

# reads the pdb file/args
def readpdb(file):
    array=[]
    with open(file, 'r') as pdb:
        for i, l in enumerate(pdb):
            # Remove odd characters and split by whitespace
            d = l.strip().split()
            # Cast the data into appropriate types
            types = [str, int, str, str, str, int, float, float, float, float, float, str]
            d = [t_i(d_i) for d_i, t_i in zip(d, types)]
            # Includes new data
            array.append(d)
    return array

#This was meant to return the atom list, but I can't seem to get it to work and don't know why.
def get_pdb_dic(lines):
    pdbdic=[]
    for line in lines:
        a={}
        a['atom']=line[0:6]
        a['atom_number']=int(line[6:11])
        a['name']=line[12:16]
        a['altloc']=line[16:17]
        a['residue_name']=line[17:20]
        a['chainID']=line[21:22]
        a['residue_number']=int(line[22:26])
        a['icode']=line[26:27]
        a['x']=float(line[30:38])
        a['y']=float(line[38:46])
        a['z']=float(line[46:54])
        a['occupancy']=float(line[54:60])
        a['temp']=float(line[60:66])
        a['element']=line[76:78].strip()
        a['mass']=getmass(a['element'])
        pdbdic.append(a)
        return pdbdic

# creates a mass dictionary for each of the element types.
def getmass(element):
    massdic = {"H": 1.01, "C": 12.01, "N": 14.01,"O": 16.0, "P": 30.97, "S": 32.07, "MG": 24.30}
    mass = massdic.get(element)
    return mass


#Funtion takes two lists of atoms from pdb files and calculates their root mean square deviation (RMSD).
def RMSD():
    file1 = readpdb("2FA9noend.pdb")
    file2 = readpdb("2FA9noend2mov.pdb")
    full = min(len(file1), len(file2))

    summation = 0
#Runs a loop over the two files and adds their square roots together according to the RMSD calculation  
    for i in range(full):
        x = (file1[i][6]-file2[i][6])**2
        y = (file1[i][7]-file2[i][7])**2
        z = (file1[i][8]-file2[i][8])**2
        total = x + y + z
        summation = summation + total
    final = ((1/full) * summation)**0.5
    return final

#returns the calculated value
print("The RMSD between your PDB structures is: ")
print(RMSD())
