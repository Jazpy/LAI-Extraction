while read i; do
  touch "${i}.fam"
  echo "${i}      ${i}" >> "${i}.fam"
done < individuals
