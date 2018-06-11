#!/bin/bash

## Job Name

#SBATCH --job-name=myjob

## Allocation Definition 
#SBATCH --account=choe 
#SBATCH --partition=choe

## Resources

## Nodes

#SBATCH --nodes=1

## Walltime (8 hours)

#SBATCH --time=8:00:00

## Memory per node

#SBATCH --mem=100G

## Specify the working directory for this job

#SBATCH --workdir=/gscratch/choe/dds/postevent

##turn on e-mail notification

#SBATCH --mail-type=ALL

#SBATCH --mail-user=qcao10@uw.edu

module load anaconda3_4.3.1 
source activate geoenv
python3 tomnod.py
