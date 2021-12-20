#!/bin/sh
rpmdev-setuptree
spectool -g -R fds.spec
rpmbuild -ba fds.spec
