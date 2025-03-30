#!/bin/bash
set -euxo pipefail
export QA_RPATHS=7
latest="6.9.1"
mkdir -p build/"$1"
cd build/"$1"
specname=$1
if [ "$1" == "latest" ]; then
    export version="$latest"
    export version_suffix=""
else
    export version="$1"
    export version_suffix="$version"
fi
export repo="$2"
export commit="$3"
export revision_date="$4"
export version_patch="$5"
export backports_patch="$6"
shift 6
mkdir -p rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}
rm rpmbuild/SOURCES/fds.sh.zip || true
zip rpmbuild/SOURCES/fds.sh.zip ../../fds.sh
cp ../../"$backports_patch" rpmbuild/SOURCES || true
cp ../../"$version_patch"  rpmbuild/SOURCES || true
cat ../../"$specname".spec ../../template.spec > fds.spec
spectool -g fds.spec -C rpmbuild/SOURCES --all \
    --define "_topdir $(pwd)/rpmbuild" \
    --define "this_version ${version}" \
    --define "repo ${repo}" \
    --define "commit ${commit}" \
    --define "revision_date ${revision_date}" \
    --define "version_patch ${version_patch}" \
    --define "backports_patch ${backports_patch}"
rpmbuild -ba fds.spec \
    --define "_topdir $(pwd)/rpmbuild" \
    --define "this_version ${version}" \
    --define "repo ${repo}" \
    --define "commit ${commit}" \
    --define "revision_date ${revision_date}" \
    --define "version_patch ${version_patch}" \
    --define "backports_patch ${backports_patch}" \
     "$@"  --noclean
mkdir -p ../../../dist
cp rpmbuild/RPMS/"$(rpmbuild --eval '%{_arch}')"/*.rpm ../../../dist/
