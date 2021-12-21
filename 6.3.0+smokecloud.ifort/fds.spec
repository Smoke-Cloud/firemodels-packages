Name:           fds-6.3.0
Version:        6.3.0
Release:        1%{?dist}
Summary:        Fire Dynamics Simulator

License:        PublicDomain
%global commit  f7f414800cb6e0829433ad150b0da71d4074ed9d
%global repo    fds-smv_deprecated
Source0:        https://github.com/firemodels/%{repo}/archive/%{commit}.zip
Patch0:         backports.patch
Url:            https://pages.nist.gov/fds-smv

BuildRequires:  intel-hpckit
BuildRequires:  intel-basekit
Requires:       bash
Requires:       intel-oneapi-runtime-libs
Requires:       intel-oneapi-mpi

%description
FDS

%prep
%setup -qc
cd %{repo}-%{commit}
%patch0 -p1

%global __brp_check_rpaths %{nil}
%global debug_package %{nil}
%build
echo "#!/bin/sh" > fds
echo "source /opt/intel/oneapi/setvars.sh" >> fds
echo "ulimit -s unlimited" >> fds
echo "exec mpiexec -np \$1 %{_bindir}/fds-exec-%{version} \"\${@:2}\"" >> fds
ls
source /opt/intel/oneapi/setvars.sh
cd %{repo}-%{commit}/FDS_Compilation/mpi_intel_linux_64
dir=$(pwd)
target=${dir##*/}
make FCOMPL=mpiifort  FOPENMPFLAGS="-qopenmp -qopenmp-link static -liomp5" VPATH="../../FDS_Source" -f ../makefile "$target"


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install %{repo}-%{commit}/FDS_Compilation/mpi_intel_linux_64/fds_mpi_intel_linux_64 $RPM_BUILD_ROOT/%{_bindir}/fds-exec-%{version}-%{version}
install fds $RPM_BUILD_ROOT/%{_bindir}/fds-%{version}

%files
%{_bindir}/fds-%{version}
%{_bindir}/fds-exec-%{version}-%{version}

%changelog
* Sat Dec 18 2021 admin
-
