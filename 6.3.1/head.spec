%global commit  352eda994c0639660ccc86bbc230b51d00592e8c
%global repo    fds-smv_deprecated
%global this_version 6.3.1
%global version_suffix %{this_version}
%global arch_suffix _64
%{!?build_openmpi:%global build_openmpi 0}
%global gnu_string mpi_gnu_linux
%global intel_string mpi_intel_linux
%global build_dir FDS_Compilation
%global openmpi_build_command \
 dir=$(pwd)
 target=${dir##*/}
 make FCOMPL=mpifort FOPENMPFLAGS="-qopenmp -qopenmp-link static -liomp5" VPATH="../../FDS_Source" -f ../makefile "$target"
%global intelmpi_build_command \
 dir=$(pwd)
 target=${dir##*/}
 make FCOMPL=mpiifort FOPENMPFLAGS="-qopenmp -qopenmp-link static -liomp5" VPATH="../../FDS_Source" -f ../makefile "$target"