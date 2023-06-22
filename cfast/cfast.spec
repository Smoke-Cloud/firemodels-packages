%global repo    cfast
%global version_dir %{this_version}
%global script_suffix %{version_suffix}
%{!?build_openmpi:%global build_openmpi 1}
%global gnu_string gnu_linux
%global intel_string intel_linux
%if "%{this_version}" <= "7.0.1"
    %global build_dir CFAST
%else
    %global build_dir Build/CFAST
%endif
%if "%{this_version}" >= "7.0.1"
    %global arch_suffix _64
%else
%endif

%global this_release 2

Name:           cfast%{?version_suffix}
Version:        %{this_version}
Release:        %{this_release}%{?dist}
Summary:        CFAST

License:        Public Domain
Source0:        https://github.com/firemodels/%{repo}/archive/%{commit}.zip
Patch0:         %{version_patch}
Patch1:         %{backports_patch}
Url:            https://pages.nist.gov/cfast

%description
CFAST

BuildRequires: make
BuildRequires: gfortran

%prep
%setup -qc
cd %{repo}-%{commit}
%patch0 -p1
%patch1 -p1

%global __brp_check_rpaths %{nil}
%global debug_package %{nil}

%build

pushd %{repo}-%{commit}/%{build_dir}/%{gnu_string}%{?arch_suffix}
export full_commit=%{commit}
export commit=${full_commit:0:9}
export build_version=%{this_version}
export REVISION_DATE=%{revision_date}
%{intelmpi_build_command}
popd


%install
rm -rf %{buildroot}
install -D %{repo}-%{commit}/%{build_dir}/%{gnu_string}%{?arch_suffix}/cfast7_linux%{?arch_suffix} %{buildroot}/%{_bindir}/cfast%{?version_suffix}

%files
%{_bindir}/cfast%{?version_suffix}

%changelog
* Tue Nov 15 2022 Jake O'Shannessy <joshannessy@smokecloud.io> - %{this_version}-2
- Correct embedded version information
* Sat Dec 18 2021 Jake O'Shannessy <joshannessy@smokecloud.io> - %{this_version}-1
- Initial package
