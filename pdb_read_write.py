import sys

#open file for reading
pdb=open("2FA9noend.pdb",'r') 
lines=pdb.readlines()


# making empty lists for inputting info later
element_list=[]
element_type=[]
original_a=[]
original_b=[]
original_c=[]
new_a=[]
new_b=[]
new_c=[]
    

#separate coordinate data from original file into x, y, z components & obtain elemental symbols as "type"
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

#format file for writing
pdb_format='{:6s}{:5d} {:^4s}{:1s} {:3s} {:1d} {:8.3f}{:8.3f}{:8.3f}{:6.2f}{:6.2f} {:>2s}\n'

#generate new file and write
output = open("writeout.pdb","w")
 
#flat_list=[item for elem in element_list for item in elem]
for l in element_list:
    output.write(pdb_format.format(*l))
output.close()
print("writeout.pdb successfully written")

sys.exit()