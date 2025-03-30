%global version_dir %{this_version}
%global script_suffix %{version_suffix}
%undefine arch_suffix
%{!?build_openmpi:%global build_openmpi 0}
%{!?build_mpich:%global build_mpich 0}
%{!?build_intelmpi:%global build_intelmpi 1}
%{!?build_docs:%global build_docs 0}
%global gnu_string ompi_gnu_linux
%global mpich_string mpich_gnu_linux
%global intel_string impi_intel_linux_openmp
%global build_dir Build
%global openmpi_build_command ./make_fds.sh
%global intelmpi_build_command \
 dir=$(pwd) \
 target=${dir##*/} \
 make INTEL_IFORT=ifx FCOMPL=mpiifx VPATH="../../Source" -f ../makefile "$target"
%global mpich_build_command \
 dir=$(pwd) \
 target=${dir##*/} \
 make VPATH="../../Source" -f ../makefile %{gnu_string}
