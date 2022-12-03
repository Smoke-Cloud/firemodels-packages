%global version_suffix %{this_version}
%global version_dir %{this_version}
%global script_suffix -%{this_version}
%undefine arch_suffix
%{!?build_openmpi:%global build_openmpi 1}
%global gnu_string ompi_gnu_linux
%global intel_string impi_intel_linux
%global build_dir Build
%global openmpi_build_command ./make_fds.sh
%global intelmpi_build_command ./make_fds.sh
