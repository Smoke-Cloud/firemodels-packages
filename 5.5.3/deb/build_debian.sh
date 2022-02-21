repo=fds
commit=bf0a6a88f318803adb96edef5c547746fc77e4a5
version=5.5.3
wget https://github.com/firemodels/${repo}/archive/${commit}.zip
unzip ${commit}.zip
pushd ${repo}-${commit}
tar -czvf ../fds_${version}.orig.tar.gz .
popd
pushd fds-${version}
tar -xzvf ../fds_${version}.orig.tar.gz
debuild --no-sign