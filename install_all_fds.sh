#!/bin/bash

set -euxo pipefail

spack install fdsc@5.5.3%oneapi
spack install fdsc@6.1.2%oneapi
spack install fdsc@6.2.0%oneapi
spack install fdsc@6.3.0%oneapi
spack install fdsc@6.3.1%oneapi
spack install fdsc@6.3.2%oneapi
spack install fdsc@6.4.0%oneapi
spack install fdsc@6.5.0%oneapi
spack install fdsc@6.5.1%oneapi
spack install fdsc@6.5.2%oneapi
spack install fdsc@6.5.3%oneapi
spack install fdsc@6.6.0%oneapi
spack install fdsc@6.7.0%oneapi
spack install fdsc@6.7.1%oneapi
spack install fdsc@6.7.3%oneapi
spack install fdsc@6.7.4%oneapi
spack install fdsc@6.7.5%oneapi
spack install fdsc@6.7.6+openmp%oneapi
spack install fdsc@6.7.7+openmp%oneapi
spack install fdsc@6.7.8%oneapi
spack install fdsc@6.7.9%oneapi
spack install fdsc@6.8.0%oneapi
spack install fdsc@6.9.0%oneapi
spack install fdsc@6.9.1%oneapi
spack install fdsc@6.10.0+hypre+sundials%oneapi^hypre@2.32.0~shared%oneapi^sundials@6.7.0+int64~shared%hypre@2.32.0~shared%oneapi
spack install fdsc@6.10.1+hypre+sundials%oneapi^hypre@2.32.0~shared%oneapi^sundials@6.7.0+int64~shared%hypre@2.32.0~shared%oneapi
# spack install fdsc@7.0.0+hypre+sundials%oneapi^hypre@3.0.0+int64^sundials@7.5.0+int64

# spack install fdsc@6.7.6+openmp%gcc
# spack install fdsc@6.7.7+openmp%gcc
# spack install fdsc@6.7.8%gcc
# spack install fdsc@6.7.9%gcc
# spack install fdsc@6.8.0%gcc
# spack install fdsc@6.9.0%gcc
# spack install fdsc@6.9.1%gcc
# spack install fdsc@6.10.0%gcc
# spack install fdsc@6.10.1%gcc
