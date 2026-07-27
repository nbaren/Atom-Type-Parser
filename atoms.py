# Basic Pseudocode:
# 1. Read file onto computer
# 2. Iterate over each column and add atom type to list
# 3. After complete, iterate over list
#    a. if it's first time seeing that atom type:
#       new key in dictionary with atom type
#       new entry value set to 1
#    b. if seen before:
#       go to that key in dictionary and increment value +1
# 4. Save that dictionary to a csv file with all the info


##### one-file prototype ###

import numpy as np
import pandas as pd

# open the file
with open("10gs_ligand.mol2", "r") as file:
    content = file.read()

    found_atom = False
    atom_lines = []

    for line in content.splitlines():
        if found_atom:
            # once we've passed the marker, start recording
            if line.startswith("@<TRIPOS>"):
                # stop if we hit the next section (e.g. @<TRIPOS>BOND)
                break
            atom_lines.append(line)
        elif "@<TRIPOS>ATOM" in line:
            found_atom = True

for line in atom_lines:
    print(line)
# while found_atom == true, collect info 
# collect data from atom until bond

# locate the atom data
# want data bw @<TRIPOS>ATOM and @<TRIPOS>BOND
# have it start recording data once it passes @<TRIPOS>ATOM
# Record entry for 6th column in a list



