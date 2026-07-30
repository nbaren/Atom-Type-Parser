import pandas as pd
import matplotlib.pyplot as plt
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

atoms_df = pd.read_csv(os.path.join(script_dir, 'atoms.csv'))
# df has columns: 'atom_type' and 'count'

# plot entire atom count data
atoms_df.plot(kind='bar', x='atom_type', y='count', title='Atom Frequency')
plt.tight_layout()
plt.savefig(os.path.join(script_dir, 'atom_frequency_full.png'))

# split atom count in middle to visualize less frequent atom distributions
midpoint = len(atoms_df) // 2
upper_half = atoms_df.iloc[:midpoint]
lower_half = atoms_df.iloc[midpoint:]

upper_half.plot(kind='bar', x='atom_type', y='count', title='Atom Frequency (Common Atoms)')
plt.tight_layout()
plt.savefig(os.path.join(script_dir, 'atom_frequency_upper_half.png'))

lower_half.plot(kind='bar', x='atom_type', y='count', title='Atom Frequency (Rare Atoms)')
plt.tight_layout()
plt.savefig(os.path.join(script_dir, 'atom_frequency_lower_half.png'))

# plot rotatable bond data
bonds_df = pd.read_csv(os.path.join(script_dir, 'rot_bonds.csv'))
bonds_df.plot(kind='bar', x='num_rotatable_bonds', y='count', title='Rotatable Bond Frequency')
plt.tight_layout()
plt.savefig(os.path.join(script_dir, 'rotatable_bond_frequency.png'))

plt.show()

