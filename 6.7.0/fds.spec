Name:           fds-6.7.0
Version:        6.7.0
Release:        2%{?dist}
Summary:        Fire Dynamics Simulator

License:        PublicDomain
%global commit  5ccea76d225537ef523709c97027cbf081f60108
%global repo    fds
Source0:        https://github.com/firemodels/%{repo}/archive/%{commit}.zip
Source1:        fds.sh.zip
Patch0:         version.patch
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
* Sat Dec 18 2021 admin
-
