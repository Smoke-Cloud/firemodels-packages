Name:           fds-6.5.3
Version:        6.5.3
Release:        1%{?dist}
Summary:        Fire Dynamics Simulator

License:        PublicDomain
Source0:        https://github.com/firemodels/fds/archive/eb56ed1a8a2205333c5b98d636226159ba063d20.zip
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
%setup -qcn fds-eb56ed1a8a2205333c5b98d636226159ba063d20
cd fds-eb56ed1a8a2205333c5b98d636226159ba063d20
%patch0 -p1

%global __brp_check_rpaths %{nil}
%global debug_package %{nil}
%build
echo "#!/bin/sh" > fds
echo "source /opt/intel/oneapi/setvars.sh" >> fds
echo "ulimit -s unlimited" >> fds
echo "exec mpiexec -np \$1 %{_bindir}/fds-exec \"\${@:2}\"" >> fds
ls
source /opt/intel/oneapi/setvars.sh

cd fds-eb56ed1a8a2205333c5b98d636226159ba063d20
cd Build/mpi_intel_linux_64
dir=$(pwd)
target=${dir##*/}
make MPIFORT=mpiifort VPATH="../../Source" -f ../makefile "$target"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install fds-eb56ed1a8a2205333c5b98d636226159ba063d20/Build/mpi_intel_linux_64/fds_mpi_intel_linux_64 $RPM_BUILD_ROOT/%{_bindir}/fds-exec-%{version}
install fds $RPM_BUILD_ROOT/%{_bindir}/fds-%{version}/fds-%{version}

%files
%{_bindir}/fds-%{version}
%{_bindir}/fds-exec-%{version}

%changelog
* Sat Dec 18 2021 admin
-
