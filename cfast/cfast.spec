%global repo    cfast
%global version_dir %{this_version}
%global script_suffix %{version_suffix}
%{!?build_openmpi:%global build_openmpi 1}
%global gnu_string gnu_linux
%global intel_string intel_linux
%if "%{this_version}" <= "7.0.1"
    %global build_dir CFAST
    %global vpath VPATH="../Source"
%else
    %global build_dir Build/CFAST
%endif
%if "%{this_version}" >= "7.0.1"
    %global arch_suffix _64
%endif

# Due to depenencies not being sufficiently ordered we need to enforce
# serial compilation.
%global parallelism -j1

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

%build

pushd %{repo}-%{commit}/%{build_dir}/%{gnu_string}%{?arch_suffix}
export full_commit=%{commit}
export commit=${full_commit:0:9}
export build_version=%{this_version}
export REVISION_DATE=%{revision_date}
export GIT_DATE=$(date "+%b %d, %Y  %T" --date='@${REVISION_DATE}')
export BUILD_DATE=$(date "+%b %d, %Y  %T" --date='@${SOURCE_DATE_EPOCH}')
%make_build %{?vpath} %{?parallelism} -f ../makefile %{gnu_string}%{?arch_suffix} \
    FFLAGS='-finit-local-zero -ffpe-trap=invalid,zero,overflow -fbacktrace %{build_fflags} -cpp -DGITHASH_PP=\"$(build_version)+g$(commit)\" -DGITDATE_PP=\""$(GIT_DATE)\"" -DBUILDDATE_PP=\""$(BUILD_DATE)\""'
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
