#!/bin/bash
set -euxo pipefail
export QA_RPATHS=7
mkdir -p build/"$1"
cd build/"$1"
export version="$1"
export commit="$2"
export revision_date="$3"
export version_patch="$4"
export backports_patch="$5"
shift 5
mkdir -p rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}
cp ../../"$version_patch" rpmbuild/SOURCES || true
cp ../../"$backports_patch" rpmbuild/SOURCES || true
cp ../../cfast.spec .
spectool -g cfast.spec -C rpmbuild/SOURCES --all \
    --define "_topdir $(pwd)/rpmbuild" \
    --define="this_version ${version}" \
    --define "commit ${commit}" \
    --define "revision_date ${revision_date}" \
    --define "version_patch ${version_patch}" \
    --define "backports_patch ${backports_patch}"
rpmbuild -ba cfast.spec \
    --define "_topdir $(pwd)/rpmbuild" \
    --define="this_version ${version}" \
    --define "commit ${commit}" \
    --define "revision_date ${revision_date}" \
    --define "version_patch ${version_patch}" \
    --define "backports_patch ${backports_patch}" \
    "$@"
mkdir -p ../../../dist
cp rpmbuild/RPMS/"$(rpmbuild --eval '%{_arch}')"/*.rpm ../../../dist/
