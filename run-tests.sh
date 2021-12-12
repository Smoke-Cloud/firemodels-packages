#!/bin/bash
set -eEuxo pipefail

err_report() {
    echo "Error on line $1"
}

trap 'err_report $LINENO' ERR

export OMP_NUM_THREADS=1

test_fds() {
    readarray -d + -t strarr <<< "$1"
    VERSION=${strarr[0]}
    echo $VERSION
    mkdir -p "test/$1" && cp "test-inputs/$VERSION.fds" "test/$1/input.fds" && pushd "test/$1" && "/opt/FDS/$1/bin/fds" 2 input.fds && popd
}

test_fds 6.1.2+smokecloud.ifort
test_fds 6.2.0+smokecloud.ifort
test_fds 6.3.0+smokecloud.ifort
test_fds 6.3.1+smokecloud.ifort
test_fds 6.3.2+smokecloud.ifort
test_fds 6.4.0+smokecloud.ifort
test_fds 6.5.0+smokecloud.ifort
test_fds 6.5.1+smokecloud.ifort
test_fds 6.5.2+smokecloud.ifort
test_fds 6.5.3+smokecloud.ifort
test_fds 6.6.0+smokecloud.ifort
test_fds 6.7.0+smokecloud.ifort
test_fds 6.7.1+smokecloud.ifort
test_fds 6.7.3+smokecloud.ifort
test_fds 6.7.4+smokecloud.ifort
test_fds 6.7.5+smokecloud.ifort
test_fds 6.7.6+smokecloud.ifort
test_fds 6.7.7+smokecloud.ifort

echo "tests run successfully"
