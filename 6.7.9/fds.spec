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

Requires:       bash

%description
FDS

%package openmpi
Summary:        Fire Dynamics Simulator with OpenMPI
BuildRequires: openmpi-devel(x86-64)
Requires: openmpi(x86-64)
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

# Build OpenMPI version
%{_openmpi_load}
{
    echo "#!/bin/sh"
    echo "module load mpi/openmpi-x86_64"
    echo "PROGRAM_VERSION=%{version}"
    echo "VERSION_SUFFIX=-%{version}"
    cat fds.sh
} > ./fds-script-openmpi
pushd %{repo}-%{commit}/Build/ompi_gnu_linux
export full_commit=%{commit}
export mpi=openmpi
export compiler=gnu
export commit=${full_commit:0:9}
./make_fds.sh
popd
%{_openmpi_unload}

# Build IntelMPI version
%{_intelmpi_load}
{
    echo "#!/bin/sh"
    echo ". /opt/intel/oneapi/setvars.sh"
    echo "PROGRAM_VERSION=%{version}"
    echo "VERSION_SUFFIX=-%{version}"
    cat fds.sh
} > ./fds-script-intelmpi
pushd %{repo}-%{commit}/Build/impi_intel_linux
export full_commit=%{commit}
export mpi=intelmpi
export compiler=intel
export commit=${full_commit:0:9}
./make_fds.sh
popd
%{_intelmpi_unload}

%install
rm -rf %{buildroot}

# Install OpenMPI version
%{_openmpi_load}
mkdir -p %{buildroot}/%{_bindir}
install %{repo}-%{commit}/Build/ompi_gnu_linux/fds_ompi_gnu_linux %{buildroot}/%{_bindir}/fds-exec-openmpi-%{version}
install fds-script-openmpi %{buildroot}/%{_bindir}/fds-openmpi-%{version}
%{_openmpi_unload}


# Install Intel MPI
%{_intelmpi_load}
mkdir -p %{buildroot}/%{_bindir}
install %{repo}-%{commit}/Build/impi_intel_linux/fds_impi_intel_linux %{buildroot}/%{_bindir}/fds-exec-intelmpi-%{version}
install fds-script-intelmpi %{buildroot}/%{_bindir}/fds-intelmpi-%{version}
%{_intelmpi_unload}

%files openmpi
%{_bindir}/fds-openmpi-%{version}
%{_bindir}/fds-exec-openmpi-%{version}

%files intelmpi
%{_bindir}/fds-intelmpi-%{version}
%{_bindir}/fds-exec-intelmpi-%{version}

%changelog
* Tue Nov 15 2022 Jake O'Shannessy <joshannessy@smokecloud.io> - 6.7.9-2
- Correct embedded version information
* Sat Dec 18 2021 Jake O'Shannessy <joshannessy@smokecloud.io> - 6.7.9-1
- Initial package
