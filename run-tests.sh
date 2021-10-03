set -eEuxo pipefail

err_report() {
    echo "Error on line $1"
}

trap 'err_report $LINENO' ERR

OMP_NUM_THREADS=1

test_fds() {
    mkdir -p test/$1 && cp room_fire.fds test/$1 && pushd test/$1 && /opt/FDS/$1/bin/fds 2 room_fire.fds && popd
}

test_diff() {
    diff test/$1 test/$2 --exclude "*_steps.csv" --exclude "*.err" --exclude "*.out" --exclude "*_git.txt" --exclude "*_cpu.csv" --exclude "*.smv"
}

test_fds 5.5.3+smokecloud.ifort

test_fds 6.1.2+smokecloud.ifort

test_fds 6.2.0+smokecloud.ifort

test_fds 6.3.0+nist.ifort
test_fds 6.3.0+smokecloud.ifort
test_diff 6.3.0+nist.ifort 6.3.0+smokecloud.ifort

test_fds 6.3.1+nist.ifort
test_fds 6.3.1+smokecloud.ifort
test_diff 6.3.1+nist.ifort 6.3.1+smokecloud.ifort

test_fds 6.3.2+nist.ifort
test_fds 6.3.2+smokecloud.ifort
test_diff 6.3.2+nist.ifort 6.3.2+smokecloud.ifort

test_fds 6.4.0+nist.ifort
test_fds 6.4.0+smokecloud.ifort
test_diff 6.4.0+nist.ifort 6.4.0+smokecloud.ifort

test_fds 6.5.0+nist.ifort
test_fds 6.5.0+smokecloud.ifort
test_diff 6.5.0+nist.ifort 6.5.0+smokecloud.ifort

test_fds 6.5.1+nist.ifort
test_fds 6.5.1+smokecloud.ifort
test_diff 6.5.1+nist.ifort 6.5.1+smokecloud.ifort

test_fds 6.5.2+nist.ifort
test_fds 6.5.2+smokecloud.ifort
test_diff 6.5.2+nist.ifort 6.5.2+smokecloud.ifort

test_fds 6.5.3+nist.ifort
test_fds 6.5.3+smokecloud.ifort
test_diff 6.5.3+nist.ifort 6.5.3+smokecloud.ifort

test_fds 6.6.0+nist.ifort
test_fds 6.6.0+smokecloud.ifort
test_diff 6.6.0+nist.ifort 6.6.0+smokecloud.ifort

test_fds 6.7.0+nist.ifort
test_fds 6.7.0+smokecloud.ifort
test_diff 6.7.0+nist.ifort 6.7.0+smokecloud.ifort

test_fds 6.7.1+nist.ifort
test_fds 6.7.1+smokecloud.ifort
test_diff 6.7.1+nist.ifort 6.7.1+smokecloud.ifort

test_fds 6.7.3+nist.ifort
test_fds 6.7.3+smokecloud.ifort
test_diff 6.7.3+nist.ifort 6.7.3+smokecloud.ifort

test_fds 6.7.4+nist.ifort
test_fds 6.7.4+smokecloud.ifort
test_diff 6.7.4+nist.ifort 6.7.4+smokecloud.ifort

test_fds 6.7.5+nist.ifort
test_fds 6.7.5+smokecloud.ifort
test_diff 6.7.6+nist.ifort 6.7.6+smokecloud.ifort

test_fds 6.7.6+nist.ifort
test_fds 6.7.6+smokecloud.ifort
test_diff 6.7.6+nist.ifort 6.7.6+smokecloud.ifort

echo "tests run successfully"