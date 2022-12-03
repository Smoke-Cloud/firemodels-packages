#!/bin/sh
export QA_RPATHS=7
mkdir -p rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}
spectool -g cfast.spec -C rpmbuild/SOURCES --all
rpmbuild -ba cfast.spec --define "_topdir $(pwd)/rpmbuild" "$@"
