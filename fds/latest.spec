%global commit  ec52dee4274fcf994d358c8b0f883eec8f67e041
%global repo    fds
%global this_version 6.7.9
%global version_dir latest
%undefine script_suffix
%undefine version_suffix
%undefine arch_suffix
%{!?build_openmpi:%global build_openmpi 0}
%global gnu_string ompi_gnu_linux
%global mpich_string mpich_gnu_linux
%global intel_string impi_intel_linux
%global build_dir Build
%global openmpi_build_command ./make_fds.sh
%global intelmpi_build_command ./make_fds.sh
