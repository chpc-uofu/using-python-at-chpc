#!/bin/bash
#SBATCH -A chpc
#SBATCH -p notchpeak-shared
#SBATCH --time=1:00:00

ml python
python plot_temperature_data.py

