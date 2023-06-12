
%global this_release 2

#TODO: this isn't as clean as the openmpi version
%global _intelmpi_load \
 . /etc/profile.d/modules.sh; \
 module use /opt/intel/oneapi/modulefiles \
 module load mpi \
 module load compiler \
 module load mkl;
%global _intelmpi_unload \
 . /etc/profile.d/modules.sh; \
 module use /opt/intel/oneapi/modulefiles \
 module unload mkl \
 module unload compiler \
 module unload mpi;

Name:           fds%{?version_suffix}
Version:        %{this_version}
Release:        %{this_release}%{?dist}
Summary:        Fire Dynamics Simulator

License:        Public Domain
Source0:        https://github.com/firemodels/%{repo}/archive/%{commit}.zip
Source1:        fds.sh.zip
Patch0:         %{version_patch}
Patch1:         %{backports_patch}
Url:            https://pages.nist.gov/fds-smv

Requires: %{name}-common = %{version}-%{release}

%description
FDS


%package common
Summary:        Fire Dynamics Simulator common files
%description common
FDS common files
Requires:       bash
Requires:       util-linux



%if %{build_openmpi}
%package openmpi
Summary:        Fire Dynamics Simulator with OpenMPI
BuildRequires: openmpi-devel
BuildRequires: make
Requires: openmpi
Requires: %{name}-common = %{version}-%{release}
%description openmpi
FDS with OpenMPI

You will need to load the openmpi-%{_arch} module to setup your path properly.
%endif

%if %{build_mpich}
%package mpich
Summary:        Fire Dynamics Simulator with OpenMPI
BuildRequires: mpich-devel
BuildRequires: make
Requires: mpich
Requires: %{name}-common = %{version}-%{release}
%description mpich
FDS with MPICH

You will need to load the mpich-%{_arch} module to setup your path properly.
%endif

%if %{build_intelmpi}
%package intelmpi
Summary:        Fire Dynamics Simulator with Intel MPI
BuildRequires:  intel-oneapi-mpi-devel
BuildRequires:  intel-oneapi-mkl-devel
BuildRequires:  intel-oneapi-compiler-fortran
# TODO: this is not always necessary
BuildRequires:  intel-oneapi-compiler-dpcpp-cpp-and-cpp-classic
BuildRequires:  make
Requires:       intel-oneapi-runtime-libs
Requires:       intel-oneapi-mpi
Requires:       %{name}-common = %{version}-%{release}
%description intelmpi
FDS with IntelMPI

%endif

%if %{build_docs}
%package doc
Summary:        FDS documentation
Group:          Productivity/Scientific/Physics
BuildArch:      noarch
Requires:       %{name}-common = %{version}-%{release}
%endif

%prep
%setup -qc
%setup -qc -a 1
cd %{repo}-%{commit}
%patch0 -p1
%patch1 -p1

%global __brp_check_rpaths %{nil}
%global debug_package %{nil}

%build

# Build common files
{
    echo "#!/bin/sh"
    echo "FDS_VERSION=%{version}"
    echo "VERSION_SUFFIX=%{version_suffix}"
    cat fds.sh
} > ./fds-script

# Build OpenMPI version
%if %{build_openmpi}
%{_openmpi_load}
pushd %{repo}-%{commit}/%{build_dir}/%{gnu_string}%{?arch_suffix}
export full_commit=%{commit}
export mpi=.openmpi
export compiler=.gnu
export commit=${full_commit:0:9}
export build_version=%{this_version}
%{openmpi_build_command}
popd
%{_openmpi_unload}
%endif

# Build MPICH version
%if %{build_mpich}
%{_mpich_load}
mkdir -p %{repo}-%{commit}/%{build_dir}/%{mpich_string}%{?arch_suffix}
pushd %{repo}-%{commit}/%{build_dir}/%{mpich_string}%{?arch_suffix}
cp %{repo}-%{commit}/%{build_dir}/%{gnu_string}%{?arch_suffix}/make_fds.sh .
export full_commit=%{commit}
export mpi=.mpich
export compiler=.gnu
export commit=${full_commit:0:9}
export build_version=%{this_version}
%{openmpi_build_command}
popd
%{_mpich_unload}
%endif

# Build IntelMPI version
%if %{build_intelmpi}
%{_intelmpi_load}
pushd %{repo}-%{commit}/%{build_dir}/%{intel_string}%{?arch_suffix}
export full_commit=%{commit}
export mpi=.intelmpi
export compiler=.intel
export mkl=.mkl
export commit=${full_commit:0:9}
export build_version=%{this_version}
%{intelmpi_build_command}
popd
%{_intelmpi_unload}
%endif

# Build docs
%if %{build_docs}
pushd %{repo}-%{commit}/Manuals
./Build_Manuals.sh
popd
%endif

%install
rm -rf %{buildroot}
echo %{buildroot}/%{_bindir}

# Install common
install -D fds-script %{buildroot}/%{_bindir}/fds%{?script_suffix}

# Install OpenMPI version
%if %{build_openmpi}
%{_openmpi_load}
install -D %{repo}-%{commit}/%{build_dir}/%{gnu_string}%{?arch_suffix}/fds%{?major_suffix}_%{gnu_string}%{?arch_suffix} %{buildroot}%{_libdir}/openmpi/bin/fds%{version_suffix}_openmpi
%{_openmpi_unload}
%endif

# Install MPICH version
%if %{build_mpich}
%{_mpich_load}
install -D %{repo}-%{commit}/%{build_dir}/%{gnu_string}%{?arch_suffix}/fds%{?major_suffix}_%{gnu_string}%{?arch_suffix} %{buildroot}%{_libdir}/mpich/bin/fds%{version_suffix}_mpich
%{_mpich_unload}
%endif

# Install Intel MPI
%if %{build_intelmpi}
%{_intelmpi_load}
install -D %{repo}-%{commit}/%{build_dir}/%{intel_string}%{?arch_suffix}/fds%{?major_suffix}_%{intel_string}%{?arch_suffix} %{buildroot}%{_libdir}/intelmpi/bin/fds%{version_suffix}_intelmpi
%{_intelmpi_unload}
%endif

%files common
%{_bindir}/fds%{?script_suffix}

%if %{build_openmpi}
%files openmpi
%{_libdir}/openmpi/bin/fds%{version_suffix}_openmpi
%endif

%if %{build_mpich}
%files mpich
%{_libdir}/mpich/bin/fds%{version_suffix}_mpich
%endif

%if %{build_intelmpi}
%files intelmpi
%{_libdir}/intelmpi/bin/fds%{version_suffix}_intelmpi
%endif

%changelog
* Tue Nov 15 2022 Jake O'Shannessy <joshannessy@smokecloud.io> - %{version}-2
- Correct embedded version information
* Sat Dec 18 2021 Jake O'Shannessy <joshannessy@smokecloud.io> - %{version}-1
- Initial package
