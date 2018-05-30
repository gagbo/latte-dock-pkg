%define nameInCapitals Latte-Dock

Name:     latte-dock
Version:  0.7.5
Release:  1%{?dist}
Summary:  Latte is a dock based on plasma frameworks

License:  GPLv2+
URL:      https://github.com/psifidotos/%{nameInCapitals}
Source0:  https://github.com/psifidotos/%{nameInCapitals}/archive/v%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-devel
BuildRequires:  libSM-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  kf5-karchive-devel
BuildRequires:  kf5-kactivities-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-kdeclarative-devel
BuildRequires:  kf5-knotifications-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kpackage-devel
BuildRequires:  kf5-plasma-devel
BuildRequires:  kf5-kwayland-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  kf5-kglobalaccel-devel
BuildRequires:  kf5-kcrash-devel

%description
Latte is a dock based on plasma frameworks that provides an elegant and
intuitive experience for your tasks and plasmoids. It animates its contents by
using parabolic zoom effect and tries to be there only when it is needed.

"Art in Coffee"

%prep
%setup -q -n %{nameInCapitals}-%{version}

%build
%{__mkdir_p} build
pushd build
%{cmake_kf5} -DCMAKE_BUILD_TYPE=Release ..
%{__make} %{?_smp_mflags}
popd

%install
make install/fast DESTDIR=%{buildroot} -C build
find %{buildroot} -size 0 -delete

# Version is wrong in latte-dock.desktop. Workaround until fixed upstream
sed -i "s/Version=%{version}/Version=1.0/" %{buildroot}/%{_datadir}/applications/org.kde.latte-dock.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.kde.latte-dock.desktop

%files
%{_bindir}/latte-dock
%{_kf5_datadir}/applications/org.kde.latte-dock.desktop
%{_datadir}/metainfo/audoban.applet.separator.appdata.xml
%{_datadir}/metainfo/org.kde.latte-dock.appdata.xml
%{_datadir}/metainfo/org.kde.latte.plasmoid.appdata.xml
%{_datadir}/metainfo/org.kde.latte.shell.appdata.xml
%{_kf5_datadir}/dbus-1/interfaces/org.kde.LatteDock.xml
%{_kf5_datadir}/icons/breeze/*/*/*
%{_kf5_datadir}/icons/hicolor/*/*/*
%{_kf5_datadir}/knotifications5/lattedock.notifyrc
%{_kf5_datadir}/kservices5/plasma-applet-org.kde.latte.containment.desktop
%{_kf5_datadir}/kservices5/plasma-applet-org.kde.latte.plasmoid.desktop
%{_kf5_datadir}/kservices5/plasma-applet-org.kde.latte.spacer.desktop
%{_kf5_datadir}/kservices5/plasma-applet-audoban.applet.separator.desktop
%{_kf5_datadir}/kservices5/plasma-shell-org.kde.latte.shell.desktop
%{_kf5_datadir}/plasma/plasmoids/org.kde.latte.containment/
%{_kf5_datadir}/plasma/plasmoids/org.kde.latte.plasmoid/
%{_kf5_datadir}/plasma/plasmoids/org.kde.latte.spacer/contents/config/config.qml
%{_kf5_datadir}/plasma/plasmoids/org.kde.latte.spacer/contents/config/main.xml
%{_kf5_datadir}/plasma/plasmoids/org.kde.latte.spacer/contents/ui/ConfigAppearance.qml
%{_kf5_datadir}/plasma/plasmoids/org.kde.latte.spacer/contents/ui/main.qml
%{_kf5_datadir}/plasma/plasmoids/org.kde.latte.spacer/metadata.desktop
%{_kf5_datadir}/plasma/plasmoids/org.kde.latte.spacer/metadata.json
%{_kf5_datadir}/plasma/plasmoids/audoban.applet.separator/contents/ui/main.qml
%{_kf5_datadir}/plasma/plasmoids/audoban.applet.separator/metadata.desktop
%{_kf5_datadir}/plasma/plasmoids/audoban.applet.separator/metadata.json
%{_kf5_datadir}/plasma/shells/org.kde.latte.shell/
%{_kf5_qmldir}/org/kde/latte/

%changelog
* Wed May 30 2018 Gerry Agbobada <gagbobada+git@gmail.com> - 0.7.5-1
- Upgrade to version 0.7.5

* Sat Feb 24 2018 Marc Deop <marc@marcdeop.com> - 0.7.3-1
- Upgrade to version 0.7.3

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.2-2
- Remove obsolete scriptlets

* Mon Nov 13 2017 Marc Deop <marc@marcdeop.com> - 0.7.2-1
- Upgrade to version 0.7.2

* Mon Oct 16 2017 Marc Deop <marc@marcdeop.com> - 0.7.1-1
- Upgrade to version 0.7.1

* Sat Aug 12 2017 Marc Deop <marc@marcdeop.com> - 0.7.0-1
- Upgrade to version 0.7.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 30 2017 Marc Deop <marc@marcdeop.com> - 0.6.2-3
- Fix spelling on %%description
- Escape macros on changelog
- Make description lines shorter
- Remove size 0 files

* Thu May 25 2017 Marc Deop <marc@marcdeop.com> - 0.6.2-2
- Follow Fedora's naming guidelines
- Remove unneeded Requires
- Drop deprecated stuff
- Do not use %%{make_install}
- Be more specific in %%files
- Add missing popd

* Wed May 10 2017 Marc Deop <marc@marcdeop.com> - 0.6.2-1
- Upgrade to version 0.6.2

* Mon May 08 2017 Marc Deop <marc@marcdeop.com> - 0.6.1-1
- Upgrade to version 0.6.1

* Fri Apr 7 2017 Marc Deop <marc@marcdeop.com> - 0.6.0-1
- Initial package.


