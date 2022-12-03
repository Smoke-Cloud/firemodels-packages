#!/bin/bash
set -euxo pipefail
while IFS="," read -r version rev date
do
   echo "Record is : $version - $rev - $date"
   ./buildrpm.sh "$version" "$rev" "$date"
done < <(tail -n +2 versions.csv)
