%global commit  5064c500c065b7abc5a34e0ae569a7ad7ec61ec8
%global repo    fds
%global this_version 6.7.6
%global version_suffix %{this_version}
%global version_dir %{this_version}
%global script_suffix -%{this_version}
%global arch_suffix _64
%{!?build_openmpi:%global build_openmpi 1}
%global gnu_string mpi_gnu_linux
%global intel_string impi_intel_linux
%global build_dir Build
%global openmpi_build_command ./make_fds.sh
%global intelmpi_build_command ./make_fds.sh
