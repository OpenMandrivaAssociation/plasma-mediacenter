Summary:	A mediacenter user interface written with the Plasma framework
Name:		plasma-mediacenter
Version:	1.3.0
Release:	2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://community.kde.org/Plasma/Plasma_Media_Center
Source0:	ftp://ftp.kde.org/pub/kde/unstable/%{name}/%{version}/src/%{name}-%{version}.tar.bz2
BuildRequires:	kdelibs4-devel
BuildRequires:	kdebase4-workspace-devel
%if %{mdvver} < 201410
BuildRequires:	nepomuk-core-devel
%else
BuildRequires:	baloo-devel
BuildRequires:	kfilemetadata-devel
%endif
BuildRequires:	qt-mobility-devel
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(taglib)
Requires:	qt-mobility

%description
A mediacenter user interface written with the Plasma framework.

%files -f %{name}.lang
%doc README LICENSE
%{_kde_bindir}/plasma-mediacenter
%{_kde_applicationsdir}/plasma-mediacenter.desktop
%{_kde_appsdir}/plasma/packages/org.kde.plasma.mediacenter/
%{_kde_libdir}/kde4/imports/org/kde/plasma/mediacenter/
%{_kde_libdir}/kde4/pmc_*.so
%{_kde_iconsdir}/hicolor/*/actions/pmc-*.*
%{_kde_iconsdir}/hicolor/*/apps/youtube-pmc.*
%{_kde_iconsdir}/hicolor/*/status/pmcnocover.*
%{_kde_services}/*.desktop
%{_kde_servicetypes}/pmc_browsingbackend.desktop
%{_kde_servicetypes}/pmc_mediasource.desktop

#----------------------------------------------------------------------------

%define plasmamediacenter_major 1.3
%define libplasmamediacenter %mklibname plasmamediacenter %{plasmamediacenter_major}

%package -n %{libplasmamediacenter}
Summary:	Shared library for %{name}
Group:		System/Libraries
# Useless
Obsoletes:	%{_lib}plasmamediacenter0.9 < 1.1.0
Obsoletes:	%{_lib}plasmamediacenter1.1 < 1.1.9
Obsoletes:	%{_lib}plasmamediacenter1.2 < 1.3.0

%description -n %{libplasmamediacenter}
Shared library for %{name}.

%files -n %{libplasmamediacenter}
%{_kde_libdir}/libplasmamediacenter.so.%{plasmamediacenter_major}*
%{_kde_libdir}/libplasmamediaadapter.so.%{plasmamediacenter_major}*

#----------------------------------------------------------------------------

%define libplasmamediacenter_devel %mklibname plasmamediacenter -d

%package -n %{libplasmamediacenter_devel}
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Requires:	%{libplasmamediacenter} = %{EVRD}

%description -n %{libplasmamediacenter_devel}
Development files for %{name}.

%files -n %{libplasmamediacenter_devel}
%{_kde_includedir}/mediacenter/
%{_kde_libdir}/libplasmamediacenter.so
%{_kde_libdir}/libplasmamediaadapter.so

#----------------------------------------------------------------------------

%prep
%setup -q -n plasma-mediacenter

%build
%cmake_kde4 -DKDE4_BUILD_TESTS=OFF -DNO_LINK_TO_PLASMA=ON
%make

%install
%makeinstall_std -C build

%find_lang %{name}

