#!/bin/sh
export QA_RPATHS=0
rpmdev-setuptree
spectool -g -R fds.spec
rpmbuild -ba fds.spec
