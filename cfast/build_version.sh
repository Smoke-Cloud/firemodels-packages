#!/bin/bash
set -euxo pipefail
export version="$1"
export repo=$(awk -F, -v version="$version" '$1 == version { print $2; exit }' versions.csv)
export commit=$(awk -F, -v version="$version" '$1 == version { print $3; exit }' versions.csv)
export date=$(awk -F, -v version="$version" '$1 == version { print $4; exit }' versions.csv)
export version_patch=$(awk -F, -v version="$version" '$1 == version { print $5; exit }' versions.csv)
export backports_patch=$(awk -F, -v version="$version" '$1 == version { print $6; exit }' versions.csv)
bash ./buildrpm.sh $version $repo $commit $date $version_patch $backports_patch
