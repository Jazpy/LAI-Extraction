import string
import glob

# Get all .bed filenames
files = glob.glob('./PopPhased/*.bed')

# Output file: individuals
out = open('./individuals', 'w')

# Iterate over all files with an unique ID
i = 0
while(i < len(files)):
        # Write the individual's ID to out
        out.write(files[i][50 : 57] + '\n')
        # Skip over this individual's other chromosome
        i = i + 2

out.close()
