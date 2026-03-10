#!/bin/bash
set -euxo pipefail
while IFS="," read -r version repo commit date version_patch backports_patch
do
   echo "Record is : $version - $commit - $date" "$version_patch" "$backports_patch"
   ./buildrpm.sh "$version" "$repo" "$commit" "$date" "$version_patch" "$backports_patch" \
         --define 'build_openmpi 1' \
         --define 'build_mpich 0' \
         --define 'build_intelmpi 0'
done < <(tail -n +2 versions.csv)
