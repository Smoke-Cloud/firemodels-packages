%global commit  eb56ed1a8a2205333c5b98d636226159ba063d20
%global repo    fds
%global this_version 6.5.3
%global version_suffix %{this_version}
%global version_dir %{this_version}
%global script_suffix -%{this_version}
%global arch_suffix _64
%{!?build_openmpi:%global build_openmpi 0}
%global gnu_string mpi_gnu_linux
%global intel_string mpi_intel_linux
%global build_dir Build
%global openmpi_build_command \
 dir=$(pwd) \
 target=${dir##*/} \
 make MPIFORT=mpifort VPATH="../../Source" -f ../makefile "$target"
%global intelmpi_build_command \
 dir=$(pwd) \
 target=${dir##*/} \
 make MPIFORT=mpiifort VPATH="../../Source" -f ../makefile "$target"
