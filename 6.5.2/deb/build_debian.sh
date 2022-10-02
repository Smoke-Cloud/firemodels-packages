repo=fds-smv_deprecated
commit=4e9103f2e61e60eb23eed8ad3397e8ac66e16216
version=6.5.2
cp ../version.patch fds-${version}/debian/patches/version || true
wget https://github.com/firemodels/${repo}/archive/${commit}.zip
unzip ${commit}.zip
pushd ${repo}-${commit}
tar -czvf ../fds-${version}_${version}.orig.tar.gz .
popd
pushd fds-${version}
tar -xzvf ../fds-${version}_${version}.orig.tar.gz
debuild --no-sign
