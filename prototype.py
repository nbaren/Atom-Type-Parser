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
from collections import Counter

def count_atom():
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

    atom_types = []

    for line in atom_lines:
        columns = line.split()  # splits on any whitespace, handles multiple spaces/tabs
        if columns:  # skip empty lines
            atom_types.append(columns[5])

    # count how many of each type there are
    type_count = Counter(atom_types)

    print(type_count)

count_atom()