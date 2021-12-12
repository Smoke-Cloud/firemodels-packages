set -euxo pipefail
pkgdir=
pkgver=6.7.3
commit=9a07c366b6439f7c5b6d89a7b3d97f117b6eeaf2
srcdir=$(pwd)
repo_name=fds

if [ ! -d "$repo_name" ]; then
    git clone https://github.com/firemodels/$repo_name
fi
cd $repo_name
git checkout $commit

source /opt/intel/oneapi/setvars.sh
cd Build/impi_intel_linux_64
./make_fds.sh

FINAL_INSTALL_DIR=/opt/FDS/$pkgver+smokecloud.ifort
INSTALLDIR=$pkgdir$FINAL_INSTALL_DIR
mkdir -p $INSTALLDIR/bin
mv fds_impi_intel_linux_64 $INSTALLDIR/bin/fds-exec

echo "#!/bin/sh" > ${INSTALLDIR}/bin/fds
echo "source /opt/intel/oneapi/setvars.sh" >> ${INSTALLDIR}/bin/fds
echo "ulimit -s unlimited" >> ${INSTALLDIR}/bin/fds
echo "exec mpiexec -np \$1 ${FINAL_INSTALL_DIR}/bin/fds-exec \"\${@:2}\"" >> ${INSTALLDIR}/bin/fds
chmod 755 ${INSTALLDIR}/bin/fds
