repo=fds
commit=71f02560677bb87dace8c81f2e5b817d24e70c46
version=6.7.5
wget https://github.com/firemodels/${repo}/archive/${commit}.zip
unzip ${commit}.zip
pushd ${repo}-${commit}
tar -czvf ../fds_${version}.orig.tar.gz .
popd
pushd fds-${version}
tar -xzvf ../fds_${version}.orig.tar.gz
debuild --no-sign
