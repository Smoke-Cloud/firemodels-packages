%global commit  a16945293f61e4de274c9bd714ceca40bb0a2028
%global repo    fds
%global this_version 6.2.0
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
