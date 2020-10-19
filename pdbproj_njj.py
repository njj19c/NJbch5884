#!python

if __name__ == '__main__':
    data = []
    with open('2FA9noend.pdb', 'r') as f:
        for i, l in enumerate(f):
            # Removes characters and split by whitespace
            d = l.strip().split()
            # Casts each data set into its appropriate format
            types = [str, int, str, str, str, int, float, float, float, float, float, str]
            d = [types[j](d[j]) for j in range(len(d))]
            # Adds the new data
            data.append(d)

    # Dictionary of average atomic masses
    mass = {'C': 12.011, 'N': 14.007, 'O': 15.999, 'S': 32.066}

    
    # Asks user what to output (Geometric Center is GC, Center of Mass is CM)
    out = input("Please type [GC] or [CM]: ")

    # The coordinates for GC or CM
    x,y,z = 0,0,0
    # Sum up mass or length of data (for the average) (total mass=tm)
    tm = 0

    # For each atom
    for d in data:
        # Obtains coordinates
        x1, y1, z1 = d[6:9]

        if out.lower() == 'gc':
            # Keep running sum
            x = x+x1
            y = y+y1
            z = z+z1
            tm += 1

        elif out.lower() == 'cm':
            # Obtain atom name and mass
            atom_name = d[-1]
            m = mass[atom_name]

            # Running sum of mass multiplied by coordinates
            x = x+(m * x1)
            y = y+(m * y1)
            z = z+(m * z1)
            tm += m
        else:
            print("Unrecognized Input. Please select GC or CM.")
            assert False

    # Normalize running sum
    x = x/tm
    y = y/tm
    z = z/tm

    
    with open('new.pdb', 'w') as f:
        for d in data:
            # Shift each coordinate by the center coordinates
            x1, y1, z1 = d[6:9]
            x1 = x1-x
            y1 = y1-y
            z1 = z1-z
            d[6:9] = x1, y1, z1

            # Writes the data to the file. I did this the python3 way instead of python2, so I hope that is fine.
            f.write( "{:6s}{:5d} {:^4s}{:1s} {:3s} {:1d} {:8.3f}{:8.3f}{:8.3f}{:6.2f}{:6.2f}          {:>2s}\n".format(*d))
