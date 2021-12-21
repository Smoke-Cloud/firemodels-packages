#!/bin/bash
set -eEuxo pipefail

err_report() {
    echo "Error on line $1"
}

trap 'err_report $LINENO' ERR

export OMP_NUM_THREADS=1

test_fds() {
    mkdir -p "test/$1" && cp "test-inputs/$1.fds" "test/$1/input.fds" && pushd "test/$1" && "fds-$1" 2 input.fds && popd
}

test_fds 5.5.3
test_fds 6.1.2
test_fds 6.2.0
test_fds 6.3.0
test_fds 6.3.1
test_fds 6.3.2
test_fds 6.4.0
test_fds 6.5.0
test_fds 6.5.1
test_fds 6.5.2
test_fds 6.5.3
test_fds 6.6.0
test_fds 6.7.0
test_fds 6.7.1
test_fds 6.7.3
test_fds 6.7.4
test_fds 6.7.5
test_fds 6.7.6
test_fds 6.7.7

echo "tests run successfully"
