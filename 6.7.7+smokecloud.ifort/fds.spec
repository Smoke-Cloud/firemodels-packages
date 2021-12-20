Name:           fds-6.7.7
Version:        6.7.7
Release:        1%{?dist}
Summary:        Fire Dynamics Simulator

License:        PublicDomain
Source0:        fds-%{version}.tar.gz
Url:            https://pages.nist.gov/fds-smv

BuildRequires:  
Requires:       bash, intel-oneapi-runtime-libs, intel-oneapi-mpi

%description
FDS

%prep
%setup -q

%global debug_package %{nil}
%build
echo "#!/bin/sh" > fds
echo "source /opt/intel/oneapi/setvars.sh" >> fds
echo "ulimit -s unlimited" >> fds
echo "exec mpiexec -np \$1 $RPM_BUILD_ROOT/%{_bindir}/fds-exec \"\${@:2}\"" >> fds

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install Build/impi_intel_linux_64/fds_impi_intel_linux_64 $RPM_BUILD_ROOT/%{_bindir}
install fds $RPM_BUILD_ROOT/%{_bindir}


FINAL_INSTALL_DIR=/opt/FDS/$pkgver+smokecloud.ifort
INSTALLDIR=$pkgdir$FINAL_INSTALL_DIR
mkdir -p $INSTALLDIR/bin


%files
%{_bindir}/fds
%{_bindir}/fds-exec


%changelog
* Sat Dec 18 2021 admin
- 
