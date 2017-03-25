#!/bin/bash
#$ -b y
#$ -w e
#$ -e ./logs_x/err
#$ -o ./logs_x/std
#$ -N extract_AFR_X  # job's name

# run the job in the current working directory
#$ -cwd

# declares the shell that interprets the job script
#$ -S /bin/bash

# all environment variables in the qsub commands environment are to be exported to the batch job
#$ -V

# reserve all requested resources
#$ -R y

module load python35/3.5.2
module load plink2/1.90beta3

python ./plink_x.py
