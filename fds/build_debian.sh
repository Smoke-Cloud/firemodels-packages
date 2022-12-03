#!/bin/bash
set -euxo pipefail

version=$1
repo=$2
commit=$3
cp ../version.patch fds-"${version}"/debian/patches/version || true
wget https://github.com/firemodels/"${repo}"/archive/"${commit}".zip
unzip "${commit}".zip
pushd "${repo}"-"${commit}"
tar -czvf ../fds-"${version}"_"${version}".orig.tar.gz .
popd
pushd fds-"${version}"
tar -xzvf ../fds-"${version}"_"${version}".orig.tar.gz
debuild --no-sign
