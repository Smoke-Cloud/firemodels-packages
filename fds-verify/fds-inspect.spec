%define baseversion 0.16.0

Name:           fds-inspect
Version:        %{baseversion}
Release:        1%{?dist}
Summary:        Binaries for FDS inspect

License:        AllRightsReserved
Source0:        fds-inspect-%{version}.tar.gz
Url:            https://smokecloud.io

BuildRequires:  cargo
Requires:       bash

%description
FDS Inpsect run server binaries

%prep
%setup -c

%global debug_package %{nil}
%build
cargo build --release \
    --bin fds-inspect

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install target/release/fds-inspect $RPM_BUILD_ROOT/%{_bindir}

%files
%{_bindir}/fds-inspect

%changelog
* Sat Dec 18 2021 admin
-
