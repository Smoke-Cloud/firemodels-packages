#!/bin/sh
export QA_RPATHS=7
mkdir -p $1
cd $1
export version=$1
export rev=$2
export revision_date=$3
shift 3
mkdir -p rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}
cp ../version.patch rpmbuild/SOURCES || true
cp ../cfast.spec .
spectool -g cfast.spec -C rpmbuild/SOURCES --all \
    --define "_topdir $(pwd)/rpmbuild" \
    --define="this_version ${version}" \
    --define "commit ${rev}" \
    --define "revision_date ${revision_date}"
rpmbuild -ba cfast.spec \
    --define "_topdir $(pwd)/rpmbuild" \
    --define="this_version ${version}" \
    --define "commit ${rev}" \
    --define "revision_date ${revision_date}" \
    "$@"
mkdir -p ../dist
cp rpmbuild/RPMS/$(rpmbuild --eval "%{_arch}")/*.rpm ../dist/
