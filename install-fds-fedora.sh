set -eEuxo pipefail

err_report() {
    echo "Error on line $1"
}

trap 'err_report $LINENO' ERR


install_fds() {
    pushd $1
    bash install-fedora.sh
}

install_fds 6.1.2+smokecloud.ifort
install_fds 6.2.0+smokecloud.ifort
install_fds 6.3.0+smokecloud.ifort
install_fds 6.3.1+smokecloud.ifort
install_fds 6.3.2+smokecloud.ifort
install_fds 6.4.0+smokecloud.ifort
install_fds 6.5.0+smokecloud.ifort
install_fds 6.5.1+smokecloud.ifort
install_fds 6.5.2+smokecloud.ifort
install_fds 6.5.3+smokecloud.ifort
install_fds 6.6.0+smokecloud.ifort
install_fds 6.7.0+smokecloud.ifort
install_fds 6.7.1+smokecloud.ifort
install_fds 6.7.3+smokecloud.ifort
install_fds 6.7.4+smokecloud.ifort
install_fds 6.7.5+smokecloud.ifort
install_fds 6.7.6+smokecloud.ifort
install_fds 6.7.7+smokecloud.ifort

echo "fds installed successfully"
