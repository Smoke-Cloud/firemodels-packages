%global version_dir %{this_version}
%undefine arch_suffix
%{!?build_openmpi:%global build_openmpi 0}
%{!?build_mpich:%global build_mpich 0}
%{!?build_intelmpi:%global build_intelmpi 1}
%{!?build_docs:%global build_docs 0}
%global build_dir Build

%global this_release 6

#TODO: this isn't as clean as the openmpi version
%global _intelmpi_load \
 export MODULES_AUTO_HANDLING=1; \
 . /etc/profile.d/modules.sh; \
 module use ~/modulefiles; \
 module load mpi/latest; \
 module load ifort; \
 module load mkl;
%global _intelmpi_unload \
 export MODULES_AUTO_HANDLING=1; \
 . /etc/profile.d/modules.sh; \
 module use ~/modulefiles; \
 module unload mkl; \
 module unload ifort; \
 module unload mpi/latest;

Name:           fds
Version:        %{this_version}
Release:        %{this_release}%{?dist}
Summary:        Fire Dynamics Simulator

License:        Public Domain
Source0:        https://github.com/firemodels/%{repo}/archive/%{commit}.zip
Source1:        fds.sh.zip
Patch0:         %{version_patch}
Patch1:         %{backports_patch}
Url:            https://pages.nist.gov/fds-smv

%description
FDS


%if %{build_openmpi}
%package openmpi
Summary:        Fire Dynamics Simulator with OpenMPI
BuildRequires: openmpi-devel
BuildRequires: make
Requires: openmpi
%description openmpi
FDS with OpenMPI

You will need to load the openmpi-%{_arch} module to setup your path properly.
%endif

%if %{build_intelmpi}
%package intelmpi
Summary:        Fire Dynamics Simulator with Intel MPI
BuildRequires:  intel-oneapi-mpi-devel
BuildRequires:  intel-oneapi-mkl-devel
BuildRequires:  intel-oneapi-compiler-fortran
%{?old_compilers:%old_compilers}
BuildRequires:  cmake
BuildRequires:  make
Requires:       intel-oneapi-runtime-libs
Requires:       intel-oneapi-mpi
%description intelmpi
FDS with IntelMPI

%endif

%if %{build_docs}
%package doc
Summary:        FDS documentation
Group:          Productivity/Scientific/Physics
BuildArch:      noarch
%description doc
Docs for FDS

%endif

%prep
%setup -n %{repo}-%{commit}

%global __brp_check_rpaths %{nil}
%global debug_package %{nil}

%build


# Build OpenMPI version
%if %{build_openmpi}
%{_openmpi_load}
export full_commit=%{commit}
export mpi=.openmpi
export compiler=.gnu
export commit=${full_commit:0:9}
export build_version=%{this_version}
%cmake
%cmake_build
%{_openmpi_unload}
%endif

# Build IntelMPI version
%if %{build_intelmpi}
%{_intelmpi_load}
export full_commit=%{commit}
export mpi=.intelmpi
export compiler=.intel
export mkl=.mkl
export commit=${full_commit:0:9}
export build_version=%{this_version}
export FC=mpiifx
%cmake
%cmake_build
%endif

%install
%cmake_install
%if %{build_openmpi}
mv $RPM_BUILD_ROOT/%{_bindir}/fds $RPM_BUILD_ROOT/%{_libdir}/openmpi/bin/fds_openmpi
%endif
%if %{build_intelmpi}
mv $RPM_BUILD_ROOT/%{_bindir}/fds $RPM_BUILD_ROOT/%{_libdir}/openmpi/bin/fds_intelmpi
%endif

%if %{build_openmpi}
%files openmpi
%{_libdir}/openmpi/bin/fds_openmpi
%endif

%if %{build_intelmpi}
%files intelmpi
%{_libdir}/intelmpi/bin/fds_intelmpi
%endif

%changelog
* Wed Apr 17 2024 Jake O'Shannessy <joshannessy@smokecloud.io> - %{version}-6
- Switch to ifx and mpiifx
* Mon Mar 25 2024 Jake O'Shannessy <joshannessy@smokecloud.io> - %{version}-5
- Unpin intel package versions
* Sun Dec 10 2023 Jake O'Shannessy <joshannessy@smokecloud.io> - %{version}-4
- Unpin intel package versions
* Mon Jul 17 2023 Jake O'Shannessy <joshannessy@smokecloud.io> - %{version}-3
- Pin intel package versions
* Tue Nov 15 2022 Jake O'Shannessy <joshannessy@smokecloud.io> - %{version}-2
- Correct embedded version information
* Sat Dec 18 2021 Jake O'Shannessy <joshannessy@smokecloud.io> - %{version}-1
- Initial package
