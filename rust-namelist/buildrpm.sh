#!/bin/bash
spec_path=rust-namelist.spec
mkdir -p rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}
cp ${spec_path} rpmbuild/SPECS/
spectool -g rpmbuild/SPECS/${spec_path} -C rpmbuild/SOURCES --all
rpmbuild -ba rpmbuild/SPECS/${spec_path} --define "_topdir $(pwd)/rpmbuild"
mkdir -p ../dist
# cp rpmbuild/RPMS/noarch/*.rpm ../dist/
