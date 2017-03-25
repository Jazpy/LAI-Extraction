import string
import glob

# Get all .bed filenames
files = glob.glob('./PopPhased/*.bed')

# Output file: individuals
out = open('./individuals', 'w')

# Iterate over all files with an unique ID
i = 0
while(i < len(files)):

    # Eliminate the "./PopPhased/" prefix
    curr_line = files[i][12:]
    # Split on first '_'
    curr_line = curr_line.split("_")[0]
    # Write the individual's ID to out
    out.write(curr_line + '\n')
    # Skip over this individual's other chromosome
    i = i + 2

out.close()
