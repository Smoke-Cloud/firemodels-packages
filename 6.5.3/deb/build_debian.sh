repo=fds
commit=eb56ed1a8a2205333c5b98d636226159ba063d20
version=6.5.3
wget https://github.com/firemodels/${repo}/archive/${commit}.zip
unzip ${commit}.zip
pushd ${repo}-${commit}
tar -czvf ../fds-${version}_${version}.orig.tar.gz .
popd
pushd fds-${version}
tar -xzvf ../fds-${version}_${version}.orig.tar.gz
debuild --no-sign
