#!/bin/sh
export QA_RPATHS=7
rpmdev-setuptree
spectool -g -R fds.spec
rpmbuild -ba fds.spec
