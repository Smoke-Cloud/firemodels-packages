#!/bin/bash
set -eEuxo pipefail

err_report() {
    echo "Error on line $1"
}

trap 'err_report $LINENO' ERR

export OMP_NUM_THREADS=1

test_cfast() {
    mkdir -p "test/$1" && cp "test-inputs/$1.in" "test/$1/input.in" && pushd "test/$1" && "cfast$1" input.in && popd
}

test_cfast 7.0.1
test_cfast 7.1.0
test_cfast 7.1.1
test_cfast 7.1.2
test_cfast 7.2.0
test_cfast 7.2.1
test_cfast 7.2.2
test_cfast 7.2.3
test_cfast 7.2.4
test_cfast 7.3.0
test_cfast 7.3.1
test_cfast 7.4.0
test_cfast 7.4.2
test_cfast 7.4.3
test_cfast 7.5.2
test_cfast 7.7.1
test_cfast 7.7.2
test_cfast 7.7.3
test_cfast 7.7.4

echo "tests run successfully"
