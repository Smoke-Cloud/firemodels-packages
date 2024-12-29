%bcond_with glui

Name:           smokeview
Version:        6.8.0
Release:        1%{?dist}
Summary:        Smokeview

%global commit e528e8b0adced1be2dba4473a8a07bab3dd6ee9b

License:        AllRightsReserved
Source0:        https://github.com/JakeOShannessy/smv/archive/%{commit}.zip
Url:            https://github.com/JakeOShannessy/smv

BuildRequires:  cmake
BuildRequires:  gd-devel
BuildRequires:  freeglut-devel
%if %{with glui}
BuildRequires:  glui-devel
%endif
BuildRequires:  libXmu-devel
BuildRequires:  glew-devel
BuildRequires:  json-c-devel

Requires:       gd
Requires:       freeglut
%if %{with glui}
Requires:       glui
%endif
Requires:       libXmu
Requires:       json-c

%description
A post-processor for FDS (Fire Dynamics Simulator).

%prep
%setup -n smv-%{commit}

%build
%cmake -DGLUI=ON -DSMV_ROOT_OVERRIDE=/usr/etc/smokeview/
%cmake_build

%install
%cmake_install

%files
%license LICENSE.md
%{_bindir}/smokeview
%{_bindir}/smokezip
%{_bindir}/smokediff
%{_bindir}/smvq
%{_bindir}/background
%{_bindir}/get_time
%{_bindir}/timep
%{_bindir}/wind2fds
%{_bindir}/flush

%{_libdir}/libglut32.so
%{_libdir}/libjsonrpc.so

%config(noreplace) /usr/etc/smokeview/smokeview.ini
%config(noreplace) /usr/etc/smokeview/objects.svo

%changelog
* Wed Jun 07 2023 Jake O'Shannessy <joshannessy@smokecloud.io> - %{version}-1
- Initial package
