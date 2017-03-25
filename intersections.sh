#!/bin/bash

#AFR
for FILE in *_A_final_AFR.bed;
do
  BASE=`basename $FILE _A_final_AFR.bed`;
  bedtools intersect -a $FILE -b $BASE\_B_final_AFR.bed -wb | awk '{if($4=="AFR" && $4==$10)print $1,$2,$3,$4":"$10}' > $BASE\_AFR-AFR.bed;
done
