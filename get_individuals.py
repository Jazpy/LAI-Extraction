import string
import glob

# Get all .bed filenames
files = glob.glob('./PopPhased/*.bed')

# Output file: individuals
out = open('./individuals', 'w')

# Iterate over all (unique) files
i = 0
while(i < len(files)):
        # Write the individual's id to out
        out.write(files[i][50 : 57] + '\n')

        i = i + 2

out.close()
