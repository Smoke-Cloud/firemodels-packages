#!/bin/bash
set -euxo pipefail
while IFS="," read -r version repo commit date version_patch backports_patch
do
   echo "Record is : $version - $commit - $date" "$version_patch" "$backports_patch"
   ./buildrpm.sh "$version" "$repo" "$commit" "$date" "$version_patch" "$backports_patch"
done < <(tail -n +2 versions.csv)
