#!/usr/bin/bash

#SBATCH -A notchpeak-shared-short
#SBATCH -p notchpeak-shared-short
#SBATCH --time=1:00:00


module load python/3.10.3
./thefuzz_demo.py
