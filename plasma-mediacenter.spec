Name:		plasma-mediacenter
Version:	1.0.0
Release:	1
Summary:	A mediacenter user interface written with the Plasma framework
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		http://community.kde.org/Plasma/Plasma_Media_Center
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{name}/%{version}/src/%{name}-%{version}.tar.gz
BuildRequires:	qt-mobility-devel
BuildRequires:	qt4-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	nepomuk-core-devel
BuildRequires:	pkgconfig(taglib)
Requires:	qt-mobility

%description
A mediacenter user interface written with the Plasma framework.

%files
%doc README LICENSE
%{_kde_appsdir}/plasma/packages/org.kde.plasma.mediacenter/
%{_kde_bindir}/plasma-mediacenter
%{_kde_applicationsdir}/plasma-mediacenter.desktop
%{_kde_services}/*.desktop
%{_kde_servicetypes}/pmc_browsingbackend.desktop
%{_kde_libdir}/kde4/imports/org/kde/plasma/mediacentercomponents/
%{_kde_libdir}/kde4/pmc_*.so

#----------------------------------------------------------------------------

%define plasmamediacenter_major 0.9
%define libplasmamediacenter %mklibname plasmamediacenter %{plasmamediacenter_major}

%package -n %{libplasmamediacenter}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n %{libplasmamediacenter}
Shared library for %{name}.

%files -n %{libplasmamediacenter}
%{_kde_libdir}/libplasmamediacenter.so.%{plasmamediacenter_major}*

#----------------------------------------------------------------------------

%define libplasmamediacenter_devel %mklibname plasmamediacenter -d

%package -n %{libplasmamediacenter_devel}
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Requires:	%{libplasmamediacenter} = %{version}-%{release}

%description -n %{libplasmamediacenter_devel}
Development files for %{name}.

%files -n %{libplasmamediacenter_devel}
%{_kde_includedir}/mediacenter/
%{_kde_libdir}/libplasmamediacenter.so

#----------------------------------------------------------------------------

%prep
%setup -q -n plasma-mediacenter

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

