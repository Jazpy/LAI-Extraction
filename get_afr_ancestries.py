# NOTE: this script needs to be run from inside the folder that contains
# PopPhased, it will store the results in a folder named AncestrySplit

import string
import glob

# Get all .bed filenames
files = glob.glob('./PopPhased/*.bed')

# Iterate over all files
for curr in files:

    # Open file and read into memory
    f = open(curr)
    lines = f.readlines()
    f.close()

    # Get the individual and chromosome without the "./PopPhased/" prefix
    curr_file = curr[12:]
    # Exclude the filename from curr_file
    curr_file = curr_file.split(".")[0]
    # AFR output file: <Individual ID>_<Chromosome>_final_AFR.bed
    out_afr = open('./AncestrySplit/' + curr_file + '_AFR.bed', 'w')

    # Generate splits
    for line in lines:

        curr_anc = line.split()[3].strip()

        if(curr_anc == 'AFR'):
            out_afr.write(line)

    out_afr.close()
