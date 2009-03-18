Summary:	Data model for the online desktop
Summary(pl.UTF-8):	Model danych dla online'owego biurka
Name:		desktop-data-model
Version:	1.2.5
Release:	2
License:	LGPL v2
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/desktop-data-model/1.2/%{name}-%{version}.tar.bz2
# Source0-md5:	23a5c7c64df1f796170d8b72201af1ab
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	dbus-devel >= 1.0.0
BuildRequires:	dbus-glib-devel >= 0.61
BuildRequires:	empathy-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-desktop-devel >= 2.10.0
BuildRequires:	gnome-vfs2-devel
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	libtool
BuildRequires:	loudmouth-devel >= 1.2.2
BuildRequires:	pcre-devel >= 6.3
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel >= 3.3
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Part of the Mugshot.org project.

%description -l pl.UTF-8
Część projektu Mugshot.org.

%package devel
Summary:	Header files for desktop-data-model library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki desktop-data-model
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-devel >= 1.0.0
Requires:	glib2-devel >= 1:2.6.0

%description devel
Header files for desktop-data-model library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki desktop-data-model.

%package static
Summary:	Static desktop-data-model library
Summary(pl.UTF-8):	Statyczna biblioteka desktop-data-model
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static desktop-data-model library.

%description static -l pl.UTF-8
Statyczna biblioteka desktop-data-model.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/desktop-data-engine
%attr(755,root,root) %{_libdir}/libddm-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libddm-1.so.0
%{_datadir}/%{name}
%{_datadir}/dbus-1/services/org.freedesktop.od.Engine.service

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libddm-1.so
%{_libdir}/libddm-1.la
%{_includedir}/ddm-1
%{_pkgconfigdir}/ddm-1.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libddm-1.a
