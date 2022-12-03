%global commit  f5004c4e1e9dc3a9ccc8644b221ca14664dea5dc
%global repo    fds-smv_deprecated
%global this_version 6.3.2
%global version_suffix %{this_version}
%global version_dir %{this_version}
%global script_suffix -%{this_version}
%global arch_suffix _64
%{!?build_openmpi:%global build_openmpi 0}
%global gnu_string mpi_gnu_linux
%global intel_string mpi_intel_linux
%global build_dir FDS_Compilation
%global openmpi_build_command \
 dir=$(pwd) \
 target=${dir##*/} \
 make FCOMPL=mpifort FOPENMPFLAGS="-qopenmp -qopenmp-link static -liomp5" VPATH="../../FDS_Source" -f ../makefile "$target"
%global intelmpi_build_command \
 dir=$(pwd) \
 target=${dir##*/} \
 make FCOMPL=mpiifort FOPENMPFLAGS="-qopenmp -qopenmp-link static -liomp5" VPATH="../../FDS_Source" -f ../makefile "$target"