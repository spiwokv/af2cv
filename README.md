# af2cv
Python script to convert Alphafold output to collective variable

## Usage:
``python af2cv.py model.gro model.pkl > plumed.dat``

model.gro - Gromacs file with the same atoms and atom numbers as in the simulation. Make sure that C-alpha atoms are labeled "CA".

model.pkl - Alphafold output pickle file. Amino acid sequence of the alphafold and Gromacs input must be the same.

## Requirements:
- python3
- pickle
- numpy

## Necessary postprocessing
- set the number of atoms in WHOLEMOLECULE to the number of atoms in the protein (default all atoms in model.gro)
- set up metadynamics or other enhanced sampling method according to Plumed documentation
- set epsilon if necessary (default no epsilon)
- set lambda (default 1000)


