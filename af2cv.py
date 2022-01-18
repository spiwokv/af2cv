import sys
import pickle
import numpy as np

if len(sys.argv) < 3:
  print("usage: python af2cv.py model.gro model.pkl > plumed.dat")
  exit()

grofile = open(sys.argv[1], 'r').readlines()
try:
  natoms = int(grofile[1])
  atoms = []
  for i in range(natoms):
    sline = str.split(grofile[i+2])
    if sline[1]=="CA":
      atoms.append(int(sline[2]))
except:
  print("Cannot read file "+sys.argv[1]+", wrong format")
  exit()

with open(sys.argv[2], 'rb') as f:
  data = pickle.load(f)
bins = data['distogram']['bin_edges']
bins = np.append(bins,2*bins[-1]-bins[-2])
logits = data['distogram']['logits']
logits = np.where(logits > 50, 50, logits)
probs = np.exp(logits)/(1.0 + np.exp(logits))
sumprobs = probs.sum(axis=2)
probs2 = probs
for i in range(len(atoms)):
  for j in range(len(atoms)):
    probs2[i,j,:] = probs[i,j,:]/sumprobs[i,j]

print("WHOLEMOLECULES ENTITY0=1-"+str(natoms))
print("ALPHA_FOLD ...")
print("LABEL=afscore")
output = "ATOMS="
for atom in atoms:
  output = output + str(atom) + ","
output = output[:-1]
print(output)
print("LAMBDA=1000")
output = "DISTANCES="
for k in range(64):
  output = output + str(bins[k]/10.0) + ","
output = output[:-1]
print(output)
for k in range(64):
  output = "LOGIT_MATRIX"+str(k)+"="
  for i in range(len(atoms)):
    for j in range(len(atoms)):
      output = output + str(probs2[i,j,k]) + ","
  output = output[:-1]
  print(output)
print("... ALPHA_FOLD")
print("PRINT ARG=afscore STRIDE=100 FILE=COLVAR")

