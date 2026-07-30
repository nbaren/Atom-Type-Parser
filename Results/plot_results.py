import pandas as pd
import matplotlib.pyplot as plt
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
plots_dir = os.path.join(script_dir, 'Plots')
os.makedirs(plots_dir, exist_ok=True)

atoms_df = pd.read_csv(os.path.join(script_dir, 'atoms.csv'))
# df has columns: 'atom_type' and 'count'

# plot entire atom count data
atoms_df.plot(kind='bar', x='atom_type', y='count', title='Atom Frequency')
plt.tight_layout()
plt.savefig(os.path.join(plots_dir, 'atom_frequency_full.png'))

# split atom count into two subsets
common_atoms = atoms_df.iloc[:20]
rare_atoms = atoms_df.iloc[20:]

common_atoms.plot(kind='bar', x='atom_type', y='count', title='Atom Frequency (Common Atoms)')
plt.tight_layout()
plt.savefig(os.path.join(plots_dir, 'atom_frequency_common.png'))

rare_atoms.plot(kind='bar', x='atom_type', y='count', title='Atom Frequency (Rare Atoms)')
plt.tight_layout()
plt.savefig(os.path.join(plots_dir, 'atom_frequency_rare.png'))

# plot rotatable bond data
bonds_df = pd.read_csv(os.path.join(script_dir, 'rot_bonds.csv'))
fig, ax = plt.subplots(figsize=(18, 6))
bonds_df.plot(kind='bar', x='num_rotatable_bonds', y='count', title='Rotatable Bond Frequency', ax=ax)

# thin out x-axis labels so they don't overlap, keeping ticks/labels aligned
ticks = ax.get_xticks()
labels = [label.get_text() for label in ax.get_xticklabels()]
ax.set_xticks(ticks[::5])
ax.set_xticklabels(labels[::5], rotation=0)

plt.tight_layout()
plt.savefig(os.path.join(plots_dir, 'rotatable_bond_frequency.png'), dpi=200)