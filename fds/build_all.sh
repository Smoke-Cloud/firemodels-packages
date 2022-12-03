#!/bin/bash
set -euxo pipefail
while IFS="," read -r version commit date version_patch
do
   echo "Record is : $version - $commit - $date" "$version_patch"
   ./buildrpm.sh "$version" "$commit" "$date" "$version_patch"
done < <(tail -n +2 versions.csv)
