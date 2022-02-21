repo=fds-smv_deprecated
commit=f5004c4e1e9dc3a9ccc8644b221ca14664dea5dc
version=6.3.2
wget https://github.com/firemodels/${repo}/archive/${commit}.zip
unzip ${commit}.zip
pushd ${repo}-${commit}
tar -czvf ../fds-${version}_${version}.orig.tar.gz .
popd
pushd fds-${version}
tar -xzvf ../fds-${version}_${version}.orig.tar.gz
debuild --no-sign
