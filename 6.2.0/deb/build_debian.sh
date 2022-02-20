repo=fds
commit=a16945293f61e4de274c9bd714ceca40bb0a2028
version=6.2.0
wget https://github.com/firemodels/${repo}/archive/${commit}.zip
unzip ${commit}.zip
pushd ${repo}-${commit}
tar -czvf ../fds_${version}.orig.tar.gz .
popd
pushd fds-${version}
tar -xzvf ../fds_${version}.orig.tar.gz
debuild --no-sign
