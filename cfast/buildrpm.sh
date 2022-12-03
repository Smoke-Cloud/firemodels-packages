#!/bin/bash
set -euxo pipefail
export QA_RPATHS=7
mkdir -p build/"$1"
cd build/"$1"
export version="$1"
export rev="$2"
export revision_date="$3"
export version_patch="$4"
shift 4
mkdir -p rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}
cp ../../"$version_patch" rpmbuild/SOURCES || true
cp ../../cfast.spec .
spectool -g cfast.spec -C rpmbuild/SOURCES --all \
    --define "_topdir $(pwd)/rpmbuild" \
    --define="this_version ${version}" \
    --define "commit ${rev}" \
    --define "revision_date ${revision_date}" \
    --define "version_patch ${version_patch}"
rpmbuild -ba cfast.spec \
    --define "_topdir $(pwd)/rpmbuild" \
    --define="this_version ${version}" \
    --define "commit ${rev}" \
    --define "revision_date ${revision_date}" \
    --define "version_patch ${version_patch}" \
    "$@"
mkdir -p ../../../dist
cp rpmbuild/RPMS/"$(rpmbuild --eval '%{_arch}')"/*.rpm ../../../dist/
