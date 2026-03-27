#!/bin/bash
set -euxo pipefail
while IFS="," read -r version repo commit date build
do
   echo "Record is : $version - $commit - $date" "$build"
   ./buildrpm.sh "$version" "$repo" "$commit" \
         --define 'build_openmpi 1' \
         --define 'build_mpich 0' \
         --define 'build_intelmpi 0'
done < <(tail -n +3 versions.csv)
