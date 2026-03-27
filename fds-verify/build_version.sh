#!/bin/bash
set -euxo pipefail
version="$1"
repo=$(awk -F, -v version="$version" '$1 == version { print $2; exit }' versions.csv)
commit=$(awk -F, -v version="$version" '$1 == version { print $3; exit }' versions.csv)
date=$(awk -F, -v version="$version" '$1 == version { print $4; exit }' versions.csv)
if [ "$repo" == "" ]; then
    echo "version: $version does not exist"
    exit 1
else
    echo "empty"
fi
bash ./buildrpm.sh "$version" "$repo" "$commit" "$date" \
         --define 'build_openmpi 1' \
         --define 'build_mpich 0' \
         --define 'build_intelmpi 0'
