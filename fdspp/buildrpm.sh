#!/bin/bash
spec_path=fdspp.spec
src_name=fdspp
version=$(rpmspec  -q --qf '%{VERSION}' ${spec_path})
mkdir -p rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}
cp ${spec_path} rpmbuild/SPECS/
git archive --output=rpmbuild/SOURCES/${src_name}-"${version}".tar.gz --prefix=${src_name}-"${version}"/ HEAD
spectool -g rpmbuild/SPECS/${spec_path} -C rpmbuild/SOURCES --all
rpmbuild -ba rpmbuild/SPECS/${spec_path} --define "_topdir $(pwd)/rpmbuild" # --with glui
mkdir -p ../dist
cp rpmbuild/RPMS/"$(rpmbuild --eval '%{_arch}')"/*.rpm ../dist/
