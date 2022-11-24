%global commit  bfaa110f1c29c157bf5f00143925c6501dd9c79a
%global repo    fds
%global this_version 6.7.4
%global version_suffix %{this_version}
%global this_release 2

#TODO: this isn't as clean as the openmpi version
%global _intelmpi_load \
 module use /opt/intel/oneapi/modulefiles \
 . /etc/profile.d/modules.sh; \
 module load mpi \
 module load compiler \
 module load mkl;
%global _intelmpi_unload \
 module use /opt/intel/oneapi/modulefiles \
 . /etc/profile.d/modules.sh; \
 module unload mkl \
 module unload compiler \
 module unload mpi;

Name:           fds%{version_suffix}
Version:        %{this_version}
Release:        %{this_release}%{?dist}
Summary:        Fire Dynamics Simulator

License:        Public Domain
Source0:        https://github.com/firemodels/%{repo}/archive/%{commit}.zip
Source1:        fds.sh.zip
Patch0:         version.patch
Url:            https://pages.nist.gov/fds-smv

Requires: %{name}-common = %{version}-%{release}

%description
FDS


%package common
Summary:        Fire Dynamics Simulator common files
%description common
FDS common files
Requires:       bash
Requires:       util-linux



%package openmpi
Summary:        Fire Dynamics Simulator with OpenMPI
BuildRequires: openmpi-devel(x86-64)
Requires: openmpi(x86-64)
Requires: %{name}-common = %{version}-%{release}
%description openmpi
FDS with OpenMPI

You will need to load the openmpi-%{_arch} module to setup your path properly.


%package intelmpi
Summary:        Fire Dynamics Simulator with Intel MPI
BuildRequires:  intel-oneapi-mpi-devel
BuildRequires:  intel-oneapi-mkl-devel
BuildRequires:  intel-oneapi-compiler-fortran
Requires:       intel-oneapi-runtime-libs
Requires:       intel-oneapi-mpi
Requires:       %{name}-common = %{version}-%{release}
%description intelmpi
FDS with IntelMPI


%prep
%setup -qc
%setup -qc -a 1
cd %{repo}-%{commit}
%patch0 -p1

%global __brp_check_rpaths %{nil}
%global debug_package %{nil}
%build
{
    echo "#!/bin/sh"
    echo "PROGRAM_VERSION=%{version}"
    echo "FDS_EXEC=fds-exec-%{version}"
    cat fds.sh
} > fds-script
source /opt/intel/oneapi/setvars.sh
cd %{repo}-%{commit}/Build/impi_intel_linux_64
export full_commit=%{commit}
export commit=${full_commit:0:9}
./make_fds.sh

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install %{repo}-%{commit}/Build/impi_intel_linux_64/fds_impi_intel_linux_64 $RPM_BUILD_ROOT/%{_bindir}/fds-exec-%{version}
install fds-script $RPM_BUILD_ROOT/%{_bindir}/fds-%{version}

%files
%{_bindir}/fds-%{version}
%{_bindir}/fds-exec-%{version}

%changelog
* Tue Nov 15 2022 Jake O'Shannessy <joshannessy@smokecloud.io> - 6.7.4-2
- Correct embedded version information
* Sat Dec 18 2021 Jake O'Shannessy <joshannessy@smokecloud.io> - 6.7.4-1
- Initial package
