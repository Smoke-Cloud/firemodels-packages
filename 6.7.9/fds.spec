Name:           fds-6.7.9
Version:        6.7.9
Release:        2%{?dist}
Summary:        Fire Dynamics Simulator

License:        Public Domain
%global commit  ec52dee4274fcf994d358c8b0f883eec8f67e041
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
cd %{repo}-%{commit}/Build/impi_intel_linux
export full_commit=%{commit}
export commit=${full_commit:0:9}
./make_fds.sh

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install %{repo}-%{commit}/Build/impi_intel_linux/fds_impi_intel_linux $RPM_BUILD_ROOT/%{_bindir}/fds-exec-%{version}
install fds-script $RPM_BUILD_ROOT/%{_bindir}/fds-%{version}

%files
%{_bindir}/fds-%{version}
%{_bindir}/fds-exec-%{version}

%changelog
* Tue Nov 15 2022 Jake O'Shannessy <joshannessy@smokecloud.io> - 6.7.9-2
- Correct embedded version information
* Sat Dec 18 2021 Jake O'Shannessy <joshannessy@smokecloud.io> - 6.7.9-1
- Initial package
