#!/bin/bash
set -euxo pipefail
version="$1"
repo=$(awk -F, -v version="$version" '$1 == version { print $2; exit }' versions.csv)
commit=$(awk -F, -v version="$version" '$1 == version { print $3; exit }' versions.csv)
date=$(awk -F, -v version="$version" '$1 == version { print $4; exit }' versions.csv)
version_patch=$(awk -F, -v version="$version" '$1 == version { print $5; exit }' versions.csv)
backports_patch=$(awk -F, -v version="$version" '$1 == version { print $6; exit }' versions.csv)
bash ./buildrpm.sh "$version" "$repo" "$commit" "$date" "$version_patch" "$backports_patch"
