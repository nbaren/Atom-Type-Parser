import numpy as np
import pandas as pd
import os
import csv
from rdkit import Chem
from rdkit.Chem import Descriptors

def parse_mol2(filepath):
    # open and read file
    with open(filepath, "r") as file:
        content = file.read()

        found_atom = False
        atom_lines = []

        # atom types:
        # extract lines between @<TRIPOS>ATOM and next @<TRIPOS> marker
        for line in content.splitlines():
            if found_atom:
                # once we've passed the marker, start recording
                if line.startswith("@<TRIPOS>"):
                    # stop if we hit the next section
                    break
                atom_lines.append(line)
            elif "@<TRIPOS>ATOM" in line:
                found_atom = True

        # add atom types to set to keep track of which types are in ligand
        atom_types = set()
        for line in atom_lines:
            columns = line.split() # split line on whitespace into list of columns
            if columns:  # skip empty lines
                atom_types.add(columns[5])

        # use RDkit to count rotatable bonds
        mol = Chem.MolFromMol2File(filepath)
        # check if mol is none
        if mol is not None:
            n_rotatable = Descriptors.NumRotatableBonds(mol)
        else:
            n_rotatable = None

    return atom_types, n_rotatable


# FUNCTION find_ligand_files(root_folder):
#     walk root_folder recursively
#     collect paths of files matching "*_ligand.mol2"
#     RETURN list of paths

def find_ligand_files(root_folder):
    ligand_paths = []


    for dirpath, dirnames, filenames in os.walk(root_folder):
        for fname in filenames:
            if fname.endswith("_ligand.mol2"):
                ligand_paths.append(os.path.join(dirpath, fname))
    return ligand_paths



def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))   # get absolute path to atoms.py folder
    root_folder = os.path.join(script_dir, "..", "PDBbind_Data")    # root folder is in atoms.py parent folder

    files = find_ligand_files(root_folder)   # collect files from PDBbind dataset

    atom_type_ligand_counts = {}   # number of ligands with each atom type
    rotatable_bond_counts = {}  # number of ligands with each number of rotatable bonds
    failed_to_parse_count = 0
    failed_files = []

    # collect info on the atom types and rotatable bonds in each ligand
    for file in files:
        atom_types, n_rotatable = parse_mol2(file)

        # update count dicts with stats from the ligand
        for atom in atom_types:
            atom_type_ligand_counts[atom] = atom_type_ligand_counts.get(atom, 0) + 1

        # keep track of how many ligands failed to parse
        if n_rotatable is None:
            failed_files.append(file)
            failed_to_parse_count += 1
            
        else:
            rotatable_bond_counts[n_rotatable] = rotatable_bond_counts.get(n_rotatable, 0) + 1

    # save the final dictionaries to CSVs for analysis
    atoms_csv_path = os.path.join(script_dir, "atoms.csv")
    rot_bonds_csv_path = os.path.join(script_dir, "rot_bonds.csv")
    failed_files_csv_path = os.path.join(script_dir, "failed_files.csv")

    with open(atoms_csv_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Row 1: Keys
        writer.writerow(atom_type_ligand_counts.keys())
        # Row 2: Values
        writer.writerow(atom_type_ligand_counts.values())

    with open(rot_bonds_csv_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(rotatable_bond_counts.keys())
        writer.writerow(rotatable_bond_counts.values())

    # save failed files and final count to CSV
    with open(failed_files_csv_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for failed_file in failed_files:
            writer.writerow([failed_file])
        writer.writerow(["failed_to_parse_count", failed_to_parse_count])

# run the script
if __name__ == "__main__":
    main()