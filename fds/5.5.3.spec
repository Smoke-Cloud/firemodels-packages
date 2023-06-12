%global version_dir %{this_version}
%global script_suffix %{version_suffix}
%global arch_suffix _64
%{!?build_openmpi:%global build_openmpi 1}
%{!?build_mpich:%global build_mpich 1}
%{!?build_intelmpi:%global build_intelmpi 1}
%{!?build_docs:%global build_docs 0}
%global gnu_string mpi_gnu_linux
%global mpich_string mpich_gnu_linux
%global intel_string mpi_intel_linux
%global build_dir FDS_Compilation
%global major_suffix 5
%global openmpi_build_command \
 dir=$(pwd) \
 target=${dir##*/} \
 make FCOMPL=mpifort FOPENMPFLAGS="-qopenmp -qopenmp-link static -liomp5" VPATH="../../FDS_Source" -f ../makefile "$target"
%global intelmpi_build_command \
 dir=$(pwd) \
 target=${dir##*/} \
 make FCOMPL=mpiifort FOPENMPFLAGS="-qopenmp -qopenmp-link static -liomp5" VPATH="../../FDS_Source" -f ../makefile "$target"
