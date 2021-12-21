Name:           fds-6.6.0
Version:        6.6.0
Release:        1%{?dist}
Summary:        Fire Dynamics Simulator

License:        PublicDomain
%global commit  88ae75a14dbfeef8d77bfcca1997878a14de5c8a
%global repo    fds
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
source /opt/intel/oneapi/setvars.sh
cd %{repo}-%{commit}
patch --forward --strip=1 --input="${srcdir}/mpi_finalize.patch" Source/main.f90 || true
cd Build/impi_intel_linux_64
./make_fds.sh

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install %{repo}-%{commit}/Build/impi_intel_linux_64/fds_impi_intel_linux_64 $RPM_BUILD_ROOT/%{_bindir}/fds-exec-%{version}
install fds $RPM_BUILD_ROOT/%{_bindir}/fds-%{version}

%files
%{_bindir}/fds-%{version}
%{_bindir}/fds-exec-%{version}

%changelog
* Sat Dec 18 2021 admin
-
