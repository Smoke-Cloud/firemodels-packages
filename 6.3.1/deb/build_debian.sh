repo=fds-smv_deprecated
commit=352eda994c0639660ccc86bbc230b51d00592e8c
version=6.3.1
cp ../version.patch fds-${version}/debian/patches/version || true
wget https://github.com/firemodels/${repo}/archive/${commit}.zip
unzip ${commit}.zip
pushd ${repo}-${commit}
tar -czvf ../fds-${version}_${version}.orig.tar.gz .
popd
pushd fds-${version}
tar -xzvf ../fds-${version}_${version}.orig.tar.gz
debuild --no-sign
