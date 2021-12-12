set -euxo pipefail
pkgdir=
pkgver=6.7.5
commit=71f02560677bb87dace8c81f2e5b817d24e70c46

if [ ! -d "fds" ]; then
    git clone https://github.com/firemodels/fds
fi
cd fds
git checkout $commit

source /opt/intel/oneapi/setvars.sh
cd Build/impi_intel_linux_64
./make_fds.sh

FINAL_INSTALL_DIR=/opt/FDS/$pkgver+smokecloud.ifort
cd fds/Build/impi_intel_linux_64
INSTALLDIR=$pkgdir$FINAL_INSTALL_DIR
mkdir -p $INSTALLDIR/bin
mv fds_impi_intel_linux_64 $INSTALLDIR/bin/fds-exec

echo "#!/bin/sh" > ${INSTALLDIR}/bin/fds
echo "source /opt/intel/oneapi/setvars.sh" >> ${INSTALLDIR}/bin/fds
echo "ulimit -s unlimited" >> ${INSTALLDIR}/bin/fds
echo "exec mpiexec -np \$1 ${FINAL_INSTALL_DIR}/bin/fds-exec \"\${@:2}\"" >> ${INSTALLDIR}/bin/fds
chmod 755 ${INSTALLDIR}/bin/fds
