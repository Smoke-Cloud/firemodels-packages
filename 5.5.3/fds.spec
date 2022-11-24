Name:           fds-5.5.3
Version:        5.5.3
Release:        2%{?dist}
Summary:        Fire Dynamics Simulator

License:        Public Domain
%global commit  bf0a6a88f318803adb96edef5c547746fc77e4a5
%global repo    fds
Source0:        https://github.com/firemodels/%{repo}/archive/%{commit}.zip
Source1:        fds.sh.zip
Patch0:         backports.patch
Patch1:         version.patch
Url:            https://pages.nist.gov/fds-smv

BuildRequires:  intel-oneapi-mpi 
BuildRequires:  intel-oneapi-mkl 
BuildRequires:  intel-oneapi-compiler-fortran
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
install %{repo}-%{commit}/FDS_Compilation/mpi_intel_linux_64/fds5_mpi_intel_linux_64 $RPM_BUILD_ROOT/%{_bindir}/fds-exec-%{version}
install fds-script $RPM_BUILD_ROOT/%{_bindir}/fds-%{version}

%files
%{_bindir}/fds-%{version}
%{_bindir}/fds-exec-%{version}

%changelog
* Tue Nov 15 2022 Jake O'Shannessy <joshannessy@smokecloud.io> - 5.5.3-2
- Correct embedded version information
* Sat Dec 18 2021 Jake O'Shannessy <joshannessy@smokecloud.io> - 5.5.3-1
- Initial package
