repo=fds-smv_deprecated
commit=9ea0a920d7816dba678888d69ff6b4393f2a850a
version=6.5.1
wget https://github.com/firemodels/${repo}/archive/${commit}.zip
unzip ${commit}.zip
pushd ${repo}-${commit}
tar -czvf ../fds-${version}_${version}.orig.tar.gz .
popd
pushd fds-${version}
tar -xzvf ../fds-${version}_${version}.orig.tar.gz
debuild --no-sign
