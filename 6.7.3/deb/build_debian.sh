repo=fds
commit=9a07c366b6439f7c5b6d89a7b3d97f117b6eeaf2
version=6.7.3
wget https://github.com/firemodels/${repo}/archive/${commit}.zip
unzip ${commit}.zip
pushd ${repo}-${commit}
tar -czvf ../fds_${version}.orig.tar.gz .
popd
pushd fds-${version}
tar -xzvf ../fds_${version}.orig.tar.gz
debuild --no-sign
