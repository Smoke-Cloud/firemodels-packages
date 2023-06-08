Name:           smokeview
Version:        6.8.0
Release:        1%{?dist}
Summary:        Smokeview

%global commit c0367f0f75fba37bcb8f27a50994de91d64c187d

License:        AllRightsReserved
Source0:        https://github.com/firemodels/smv/archive/%{commit}.zip
Url:            https://github.com/firemodels/smv

BuildRequires:  systemd, systemd-rpm-macros
BuildRequires:  cmake, gd-devel, freeglut-devel, glui-devel
Requires:       bash
Requires:       lua-filesystem
Requires:       lua
Requires:       gd, freeglut, glui

%description
A post-processor for FDS (Fire Dynamics Simulator).

%prep
%setup -n smv-%{commit}

%global debug_package %{nil}
%build
%cmake -DLUA=ON -DGLUI=ON -DLUA_BUILD_BINARY=OFF -DCMAKE_INSTALL_LIBDIR=lib64
%cmake_build

%install
%cmake_install

%files
%{_bindir}/smokeview
%{_bindir}/smokezip
%{_bindir}/smokediff
%{_datadir}/*.lua
%{_libdir}/lfs.so
%{_libdir}/lpeg.so
%{_libdir}/lua.so

%changelog
* Wed Jun 07 2023 Jake O'Shannessy <joshannessy@smokecloud.io> - %{version}-1
- Initial package
