
%global commit  31ef0951cd827fb7f08b090b716a00f6288c8eb5
%global repo    cfast
%global this_version 7.2.3
%global version_suffix %{this_version}
%global version_dir %{this_version}
%global script_suffix -%{this_version}
%global arch_suffix _64
%{!?build_openmpi:%global build_openmpi 1}
%global gnu_string gnu_linux
%global intel_string intel_linux
%global build_dir Build/CFAST
%global openmpi_build_command ./make_cfast.sh
%global intelmpi_build_command ./make_cfast.sh

%global this_release 2

#TODO: this isn't as clean as the openmpi version
%global _intelmpi_load \
 . /etc/profile.d/modules.sh; \
 module use /opt/intel/oneapi/modulefiles \
 module load mpi \
 module load compiler \
 module load mkl;
%global _intelmpi_unload \
 . /etc/profile.d/modules.sh; \
 module use /opt/intel/oneapi/modulefiles \
 module unload mkl \
 module unload compiler \
 module unload mpi;

Name:           cfast
Version:        7.2.3
Release:        %{this_release}%{?dist}
Summary:        CFAST

License:        Public Domain
Source0:        https://github.com/firemodels/%{repo}/archive/%{commit}.zip
Url:            https://pages.nist.gov/cfast

%description
FDS

BuildRequires: make

%prep
%setup -qc
cd %{repo}-%{commit}

%global __brp_check_rpaths %{nil}
%global debug_package %{nil}

%build

pushd %{repo}-%{commit}/%{build_dir}/%{gnu_string}%{?arch_suffix}
export full_commit=%{commit}
export mpi=openmpi
export compiler=gnu
export commit=${full_commit:0:9}
%{openmpi_build_command}
popd


%install
rm -rf %{buildroot}
install -D %{repo}-%{commit}/%{build_dir}/%{gnu_string}%{?arch_suffix}/cfast7_linux%{?arch_suffix} %{buildroot}/%{_bindir}/cfast

%files
%{_bindir}/cfast

%changelog
* Tue Nov 15 2022 Jake O'Shannessy <joshannessy@smokecloud.io> - 6.1.1-2
- Correct embedded version information
* Sat Dec 18 2021 Jake O'Shannessy <joshannessy@smokecloud.io> - 6.1.1-1
- Initial package
