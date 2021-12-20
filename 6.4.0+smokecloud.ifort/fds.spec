Name:           fds-6.4.0
Version:        6.4.0
Release:        1%{?dist}
Summary:        Fire Dynamics Simulator

License:        PublicDomain
Source0:        https://github.com/firemodels/fds/archive/refs/tags/FDS%{version}.tar.gz
Url:            https://pages.nist.gov/fds-smv

BuildRequires:  intel-hpckit, intel-basekit
Requires:       bash, intel-oneapi-runtime-libs, intel-oneapi-mpi

%description
FDS

%prep
%setup -c

%global __brp_check_rpaths %{nil}
%global debug_package %{nil}
%build
echo "#!/bin/sh" > fds
echo "source /opt/intel/oneapi/setvars.sh" >> fds
echo "ulimit -s unlimited" >> fds
echo "exec mpiexec -np \$1 %{_bindir}/fds-exec \"\${@:2}\"" >> fds
ls
source /opt/intel/oneapi/setvars.sh
cd fds-FDS%{version}/Build/impi_intel_linux_64
./make_fds.sh

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install fds-FDS%{version}/Build/impi_intel_linux_64/fds_impi_intel_linux_64 $RPM_BUILD_ROOT/%{_bindir}/fds-exec
install fds $RPM_BUILD_ROOT/%{_bindir}

%files
%{_bindir}/fds
%{_bindir}/fds-exec

%changelog
* Sat Dec 18 2021 admin
-
