repo=fds
commit=fe0d4ef38f955b2a298ac9124ea3d8f085704edd
version=6.7.7
cp ../version.patch fds-${version}/debian/patches/version || true
wget https://github.com/firemodels/${repo}/archive/${commit}.zip
unzip ${commit}.zip
pushd ${repo}-${commit}
tar -czvf ../fds-${version}_${version}.orig.tar.gz .
popd
pushd fds-${version}
tar -xzvf ../fds-${version}_${version}.orig.tar.gz
debuild --no-sign
