Name:           fds-6.3.2
Version:        6.3.2
Release:        2%{?dist}
Summary:        Fire Dynamics Simulator

License:        Public Domain
%global commit  f5004c4e1e9dc3a9ccc8644b221ca14664dea5dc
%global repo    fds-smv_deprecated
Source0:        https://github.com/firemodels/%{repo}/archive/%{commit}.zip
Source1:        fds.sh.zip
Patch0:         backports.patch
Patch1:         version.patch
Url:            https://pages.nist.gov/fds-smv

BuildRequires:  intel-hpckit
BuildRequires:  intel-basekit
BuildRequires:  make
Requires:       bash
Requires:       intel-oneapi-runtime-libs
Requires:       intel-oneapi-mpi

%description
FDS

%prep
%setup -qc
%setup -qc -a 1
cd %{repo}-%{commit}
%patch0 -p1
%patch1 -p1

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
cd %{repo}-%{commit}/FDS_Compilation/mpi_intel_linux_64
export full_commit=%{commit}
export commit=${full_commit:0:9}
dir=$(pwd)
target=${dir##*/}
make FCOMPL=mpiifort  FOPENMPFLAGS="-qopenmp -qopenmp-link static -liomp5" VPATH="../../FDS_Source" -f ../makefile "$target"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install %{repo}-%{commit}/FDS_Compilation/mpi_intel_linux_64/fds_mpi_intel_linux_64 $RPM_BUILD_ROOT/%{_bindir}/fds-exec-%{version}
install fds-script $RPM_BUILD_ROOT/%{_bindir}/fds-%{version}

%files
%{_bindir}/fds-%{version}
%{_bindir}/fds-exec-%{version}

%changelog
* Tue Nov 15 2022 Jake O'Shannessy <joshannessy@smokecloud.io> - 6.3.2-2
- Correct embedded version information
* Sat Dec 18 2021 Jake O'Shannessy <joshannessy@smokecloud.io> - 6.3.2-2
- Initial package
