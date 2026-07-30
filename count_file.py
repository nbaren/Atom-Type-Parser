"""This is just because I forgot to count how many ligand files there were in my program"""
import os

script_dir = os.path.dirname(os.path.abspath(__file__))   # get absolute path to count_file.py folder
root_folder = os.path.join(script_dir, "..", "PDBbind_Data")    # root folder is in count_file.py parent folder

num_files = 0

for dirpath, dirnames, filenames in os.walk(root_folder):
        for fname in filenames:
            if fname.endswith("_ligand.mol2"):
                 num_files += 1

num_files_path = os.path.join(script_dir, "Results/num_ligands.txt")

with open(num_files_path, "w", newline="", encoding="utf-8") as file:
     file.write(f"Number of ligand files: {num_files}")