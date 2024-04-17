%global version_dir %{this_version}
%global script_suffix %{version_suffix}
%global arch_suffix _64
%{!?build_openmpi:%global build_openmpi 0}
%{!?build_mpich:%global build_mpich 0}
%{!?build_intelmpi:%global build_intelmpi 1}
%{!?build_docs:%global build_docs 0}
%global gnu_string mpi_gnu_linux
%global mpich_string mpich_gnu_linux
%global intel_string mpi_intel_linux
%global build_dir Build
%global openmpi_build_command \
 dir=$(pwd) \
 target=${dir##*/} \
 make MPIFORT=mpifort VPATH="../../Source" -f ../makefile "$target"
%global intelmpi_build_command \
 dir=$(pwd) \
 target=${dir##*/} \
 make INTEL_IFORT=ifx FCOMPL=mpiifx VPATH="../../Source" -f ../makefile "$target"
%global mpich_build_command \
 dir=$(pwd) \
 target=${dir##*/} \
 make MPIFORT=mpifort VPATH="../../Source" -f ../makefile %{gnu_string}%{arch_suffix}
