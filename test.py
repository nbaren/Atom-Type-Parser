"""
test.py — just for fun, written by Claude (Cowork mode) at Greg's request.
Not part of the real pipeline. Delete anytime.
"""

import random

GREG_FACTS = [
    "is currently parsing thousands of mol2 files and not going insane.",
    "knows the difference between a set and a list now. Big day.",
    "is about to make RDKit do all the hard rotatable-bond math.",
    "has a folder called 'Atoms' which is a great band name.",
]

MOLECULE_PEP_TALKS = [
    "You have {n} atoms and every single one of them is rotatable in spirit.",
    "Not all bonds are rotatable, but this one believes in itself.",
    "Somewhere, a ligand is proud of you.",
    "C.ar, C.3, N.am — doesn't matter the type, you're all valid atoms.",
]


def roast_the_dataset(n_ligands=19443):
    print(f"PDBbind has about {n_ligands} ligands.")
    print("That's a lot of mol2 files for one person to hardcode by hand.")
    print("Good thing you're not doing that anymore.\n")


def pep_talk(n_atoms=None):
    if n_atoms is None:
        n_atoms = random.randint(20, 80)
    msg = random.choice(MOLECULE_PEP_TALKS).format(n=n_atoms)
    print(f"[{n_atoms} atoms]: {msg}")


def greg_fact():
    print("Greg " + random.choice(GREG_FACTS))


if __name__ == "__main__":
    print("=" * 50)
    print("  test.py — a completely unnecessary detour")
    print("=" * 50)
    roast_the_dataset()
    greg_fact()
    pep_talk()
    print("\nOkay, back to the real code.")
