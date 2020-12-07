import matplotlib.pyplot as plt

import numpy as np

import math
# User input to give a filename. Read the file. Then plot it. Show it and save it.


rrvalues=[]
plt.figure(0)

while 1:
    arg = input("Enter filename (or q for quit): ")

# asks for a file or files to input for analysis
  
  
    if arg == 'q':
        break

    data = np.loadtxt(arg,delimiter=',') #loads and assigns the file array to values for calulations and plotting
    Voltage = data[:,0]
    Current = data[:,1]
    Adjusted_Current = Current*(10**9)
    
    #equations and values for calculating nanopipette tip diameters
    Resistance=(-0.5/data[0,1])
    radius=1/((np.pi)*(10.862)*(Resistance)*math.tan(3))
    diameter=(2*radius)*1000000000
    Resistencecheck=(-0.5/data[2000,1])
    radiuscheck=1/((np.pi)*(10.862)*(Resistencecheck)*math.tan(3))
    diameter_check=(2*radiuscheck)*1000000000
    diameter_average=(diameter+diameter_check)/(2)
    print(diameter_average)

    
    #calculates rectification ratio equation and values
    rectification_ratio=abs(data[1000,1])/(data[0,1])
    rectification_ratio2=abs(data[3000,1])/(data[2000,1])
    rectification_ratio3=abs(data[5000,1])/(data[4000,1])
    rav=(rectification_ratio+rectification_ratio2+rectification_ratio3)/3
    rrvalues.append(rav)
    print(rav)
    plt.plot(Voltage,Adjusted_Current, label=arg)


plt.legend()
plt.title("Nanopipette Cyclic Voltammagram")
plt.ylabel("Current (nA)")
plt.xlabel("Potential (V)")
plt.savefig('out.png')
plt.show()

plt.figure(1)
for x,r in enumerate(rrvalues):
    plt.scatter(x,r, label='file {}'.format(x)) #plots rectification values together for comparison
plt.legend()
plt.ylabel("")
plt.xlabel("")
plt.title("Change in Rectification")
plt.savefig('out2.png')
plt.show()