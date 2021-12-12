#!/bin/bash
source /opt/intel/oneapi/setvars.sh
set -euxo pipefail
pkgdir=
pkgver=6.4.0
commit=59962898c0dbd5926605eed69ed2690c720ca001
srcdir=$(pwd)
repo_name=fds-smv_deprecated

if [ ! -d "$repo_name" ]; then
    git clone https://github.com/firemodels/$repo_name
fi
pushd $repo_name
git checkout $commit

patch --forward --strip=1 --input="${srcdir}/backports.patch" --directory FDS_Source --strip 2 || true
cd FDS_Compilation/mpi_intel_linux_64
platform=intel64
dir=$(pwd)
target=${dir##*/}
make -j4 FCOMPL=mpiifort FOPENMPFLAGS="-qopenmp -qopenmp-link static -liomp5" VPATH="../../FDS_Source" -f ../makefile $target

FINAL_INSTALL_DIR=/opt/FDS/$pkgver+smokecloud.ifort
INSTALLDIR=$pkgdir$FINAL_INSTALL_DIR
mkdir -p $INSTALLDIR/bin
mv fds_impi_intel_linux_64 $INSTALLDIR/bin/fds-exec

echo "#!/bin/sh" > ${INSTALLDIR}/bin/fds
echo "source /opt/intel/oneapi/setvars.sh" >> ${INSTALLDIR}/bin/fds
echo "ulimit -s unlimited" >> ${INSTALLDIR}/bin/fds
echo "exec mpiexec -np \$1 ${FINAL_INSTALL_DIR}/bin/fds-exec \"\${@:2}\"" >> ${INSTALLDIR}/bin/fds
chmod 755 ${INSTALLDIR}/bin/fds
popd