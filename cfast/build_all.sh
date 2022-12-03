#!/bin/bash
set -euxo pipefail
mkdir -p ../dist/
while IFS="," read -r version commit date version_patch
do
   echo "Record is : $version - $commit - $date" "$version_patch"
   ./buildrpm.sh "$version" "$commit" "$date" "$version_patch"
   cp build/"$version"/rpmbuild/RPMS/"$(rpmbuild --eval '%{_arch}')"/*.rpm ../dist/
done < <(tail -n +2 versions.csv)
