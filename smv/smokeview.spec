Name:           smokeview
Version:        6.8.0
Release:        1%{?dist}
Summary:        Smokeview

%global commit 9f82628646f4295e47f3058ea932eb680a416b7a

License:        AllRightsReserved
Source0:        https://github.com/firemodels/smv/archive/%{commit}.zip
Url:            https://github.com/firemodels/smv

BuildRequires:  cmake, gd-devel, freeglut-devel, glui-devel, libXmu-devel, lua-devel
Requires:       bash
Requires:       lua-filesystem
Requires:       lua
Requires:       gd, freeglut, glui, libXmu

%description
A post-processor for FDS (Fire Dynamics Simulator).

%prep
%setup -n smv-%{commit}

%global debug_package %{nil}
%build
%cmake -DLUA=ON -DGLUI=ON
%cmake_build

%install
%cmake_install

%files
%{_bindir}/smokeview
%{_bindir}/smokezip
%{_bindir}/smokediff
%{_datadir}/smokeview/*.lua

%changelog
* Wed Jun 07 2023 Jake O'Shannessy <joshannessy@smokecloud.io> - %{version}-1
- Initial package
