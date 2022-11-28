%global commit  bf0a6a88f318803adb96edef5c547746fc77e4a5
%global repo    fds
%global this_version 5.5.3
%global version_suffix %{this_version}
%global arch_suffix _64
%{!?build_openmpi:%global build_openmpi 0}
%global gnu_string mpi_gnu_linux
%global intel_string mpi_intel_linux
%global build_dir FDS_Compilation
%global major_suffix 5
%global openmpi_build_command \
 dir=$(pwd)
 target=${dir##*/}
 make FCOMPL=mpifort FOPENMPFLAGS="-qopenmp -qopenmp-link static -liomp5" VPATH="../../FDS_Source" -f ../makefile "$target"
%global intelmpi_build_command \
 dir=$(pwd)
 target=${dir##*/}
 make FCOMPL=mpiifort FOPENMPFLAGS="-qopenmp -qopenmp-link static -liomp5" VPATH="../../FDS_Source" -f ../makefile "$target"
