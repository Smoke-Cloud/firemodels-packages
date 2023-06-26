Name:           smokeview
Version:        6.8.0
Release:        1%{?dist}
Summary:        Smokeview

%global commit 24bb184dacf75626399537772460477597d2443a
%global bot_commit 2cafc15b8a2797df0ff8fe3f64ab44c1719b5db5

License:        AllRightsReserved
Source0:        https://github.com/firemodels/smv/archive/%{commit}.zip
Source1:        https://github.com/firemodels/bot/archive/%{bot_commit}.zip
Url:            https://github.com/firemodels/smv

BuildRequires:  cmake, gd-devel, freeglut-devel, glui-devel, libXmu-devel, lua-devel, glew-devel
Requires:       bash
Requires:       lua-filesystem
Requires:       lua
Requires:       gd, freeglut, glui, libXmu

%description
A post-processor for FDS (Fire Dynamics Simulator).

%prep
%setup -n smv-%{commit} -a 1

%build
%cmake -DLUA=ON -DGLUI=ON
%cmake_build

%global for_bundle bot-%{bot_commit}/Bundlebot/smv/for_bundle

%install
%cmake_install
install -D -m 644 %{for_bundle}/smokeview.ini %{buildroot}/%{_sysconfdir}/smokeview/smokeview.ini
install -D -m 644 %{for_bundle}/objects.svo %{buildroot}/%{_sysconfdir}/smokeview/objects.svo

%files
%{_bindir}/smokeview
%{_bindir}/smokezip
%{_bindir}/smokediff
%{_datadir}/smokeview/*.lua
%config(noreplace) %{_sysconfdir}/smokeview/smokeview.ini
%config(noreplace) %{_sysconfdir}/smokeview/objects.svo

%changelog
* Wed Jun 07 2023 Jake O'Shannessy <joshannessy@smokecloud.io> - %{version}-1
- Initial package
