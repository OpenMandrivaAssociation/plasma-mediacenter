%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Plasma 5 media center
Name:		plasma-mediacenter
Version:	5.6.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/
Source0:	http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Activities)
BuildRequires:	cmake(KF5Baloo)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5FileMetaData)
BuildRequires:	cmake(KF5GuiAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5PlasmaQuick)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Multimedia)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(taglib)
Requires:	plasma-shell-mediacenter
Requires:	plasma-workspace
Requires:	qt5-qtmultimedia

%description
Plasma 5 media center.

%files -f plasma-mediacenter.lang
%{_datadir}/applications/plasma-mediacenter.desktop
%{_datadir}/xsessions/plasma-mediacenter.desktop
%{_iconsdir}/hicolor/*/actions/pmc-back.*
%{_datadir}/kservicetypes5/*.desktop
%{_libdir}/qt5/plugins/plasma/mediacenter/browsingbackends/pmc_metadatamusicbackend.so
%{_libdir}/qt5/plugins/plasma/mediacenter/browsingbackends/pmc_metadatapicturebackend.so
%{_libdir}/qt5/plugins/plasma/mediacenter/browsingbackends/pmc_metadatavideobackend.so
%{_libdir}/qt5/plugins/plasma/mediacenter/datasources/pmc_baloosearch.so
%{_libdir}/qt5/plugins/plasma/mediacenter/datasources/pmc_filesystemsearch.so
%{_libdir}/qt5/plugins/plasma/mediacenter/datasources/pmc_lastfm.so
%dir %{_libdir}/qt5/qml/org/kde/plasma/mediacenter/
%{_libdir}/qt5/qml/org/kde/plasma/mediacenter/*

#----------------------------------------------------------------------------

%package -n plasma-shell-mediacenter
Summary:	Plasma 5 media center shell
Group:		Graphical desktop/KDE
# Not sure if it's required
Suggests:	%{name}

%description -n plasma-shell-mediacenter
Plasma 5 media center shell.

%files -n plasma-shell-mediacenter -f plasma_shell_org.kde.plasma.mediacenter.lang
%dir %{_datadir}/plasma/shells/org.kde.plasma.mediacenter/
%{_datadir}/plasma/shells/org.kde.plasma.mediacenter/*
%{_datadir}/kservices5/plasma-shell-org.kde.plasma.mediacenter.desktop

#----------------------------------------------------------------------------

%define plasmamediacenter_major 5
%define libplasmamediacenter %mklibname plasmamediacenter %{plasmamediacenter_major}

%package -n %{libplasmamediacenter}
Summary:	Plasma 5 media center shared library
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libplasmamediacenter}
Plasma 5 media center shared library.

%files -n %{libplasmamediacenter}
%{_libdir}/libplasmamediacenter.so.%{plasmamediacenter_major}
%{_libdir}/libplasmamediacenter.so.%{version}

#----------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang plasma-mediacenter
%find_lang plasma_shell_org.kde.plasma.mediacenter
