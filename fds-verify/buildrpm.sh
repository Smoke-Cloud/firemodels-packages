#!/bin/bash
set -euxo pipefail
export QA_RPATHS=7
latest="latest"
mkdir -p build/"$1"
zip build/fds.sh.zip fds.sh
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
shift 4
mkdir -p rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}
cp ../../"fds-$version.patch"  rpmbuild/SOURCES
cat  ../../template.spec > fds.spec
spectool -g fds.spec -C rpmbuild/SOURCES --all \
    --define "_topdir $(pwd)/rpmbuild" \
    --define "this_version ${version}" \
    --define "repo ${repo}" \
    --define "commit ${commit}" \
    --define "revision_date ${revision_date}" \
    --define "version_suffix ${version_suffix}"
rpmbuild -ba fds.spec \
    --define "_topdir $(pwd)/rpmbuild" \
    --define "this_version ${version}" \
    --define "repo ${repo}" \
    --define "commit ${commit}" \
    --define "revision_date ${revision_date}" \
    --define "version_suffix ${version_suffix}" \
     "$@"  --noclean
mkdir -p ../../../dist
cp rpmbuild/RPMS/"$(rpmbuild --eval '%{_arch}')"/*.rpm ../../../dist/
