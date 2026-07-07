#!/bin/bash
set -euxo pipefail
src_name=fds-inspect
version=0.16.0
# git config --global --add safe.directory /__w/smoke-cloud-server/smoke-cloud-server
git archive --output=build/inspect/rpmbuild/SOURCES/"${src_name}"-"${version}".tar.gz --prefix="${src_name}"-"${version}"/ HEAD
export QA_RPATHS=7
mkdir -p build/inspect
cd build/inspect
mkdir -p rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}
spec_path=../../fds-inspect.spec
cp ${spec_path} rpmbuild/SPECS/
spectool -g  rpmbuild/SPECS/fds-inspect.spec -C rpmbuild/SOURCES --all \
    --define "_topdir $(pwd)/rpmbuild"
rpmbuild -ba  rpmbuild/SPECS/fds-inspect.spec \
    --define "_topdir $(pwd)/rpmbuild" \
     "$@"  --noclean
mkdir -p ../../../dist
cp rpmbuild/RPMS/"$(rpmbuild --eval '%{_arch}')"/*.rpm ../../../dist/
