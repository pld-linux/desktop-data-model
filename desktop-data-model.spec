Summary:	Data model for the online desktop
Summary(pl.UTF-8):	Model danych dla online'owego biurka
Name:		desktop-data-model
Version:	1.2.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/desktop-data-model/1.2/%{name}-%{version}.tar.bz2
# Source0-md5:	40a48937210f832b067ed590efea7ad0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-devel >= 1.0
BuildRequires:	dbus-glib-devel >= 0.61
BuildRequires:	glib2-devel >= 1:2.6
BuildRequires:	gnome-desktop-devel >= 2.10.0
BuildRequires:	gtk+2-devel >= 2:2.10
BuildRequires:	libtool
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel
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

%description devel
Header files for desktop-data-model library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki desktop-data-model.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
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
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/lib*.so.*
%{_datadir}/%{name}
%{_datadir}/dbus-1/services/*.service

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/ddm-1
%{_pkgconfigdir}/*.pc
