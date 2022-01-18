# af2cv
Python script to convert Alphafold output to collective variable

## Usage:

 python af2cv.py model.gro model.pkl > plumed.dat

model.gro - Gromacs file with the same atoms and atom numbers as in the simulation. Make sure that C-alpha atoms must be labeled as "CA".

model.pkl - Alphafold output pickle file. Amino acid sequence of the alphafold output and Gromacs input must be the same.

## Requirements:

- python3
- pickle
- numpy


