import string
import subprocess

import sys

# Open file with IDs for individuals, load into a list
f = open('individuals')
ids = f.readlines()
f.close()

# Iterate over IDs
for ind in ids:

    ind = ind.strip()

    # Extract for the chromosome given in command line arg
    # String with current chromosome file
    chro_path = '/mnt/Archives/genome/1000genomes/release_20130502/ALL.chr' + str(sys.argv[1])
    chro_path += '.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz'

    # String for .fam file
    fam_path = './fam_individuals/' + ind + '.fam'

    # String for .bed file, tied to the individual
    bed_path = './AncestrySplit/AFR-AFR/' + ind + '_AFR-AFR.bed'

    # String for output path
    out_path = './AFR_EXTRACTED/' + ind + str(sys.argv[1]) + '_AFR-AFR'

    # System call to plink
    subprocess.call(['plink', '--noweb', '--vcf', chro_path, '--keep', fam_path,
        '--extract', 'range', bed_path, '--make-bed', '--out', out_path, '--chr', str(sys.argv[1])])
