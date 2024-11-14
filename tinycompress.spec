%define major		0
%define libname		%mklibname %{name} %{major}
%define libname_devel	%mklibname %{name} -d

Name:		tinycompress
Version:	1.2.13
Release:	1
Summary:	Userspace Interface to Kernel ALSA Compressed Audio APIs
Group:		Sound/Utilities
License:	BSD and LGPLv2
URL:		https://alsa-project.org/
Source0:	ftp://ftp.alsa-project.org/pub/tinycompress/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(alsa)
BuildRequires:	kernel-headers

%description
Userspace library for anyone who wants to use the ALSA compressed APIs
introduced in Linux 3.3

This library provides the APIs to open a ALSA compressed device and read/write
compressed data like MP3 etc to it.

This also includes a utility command line player (cplay) which demonstrates 
the usage of this API. Currently this contains support for playing the mp3 format

%package -n %{libname}
Summary:	Userspace Interface to Kernel ALSA Compressed Audio APIs
Group:		System/Libraries

%description -n %{libname}
Userspace library for anyone who wants to use the ALSA compressed APIs
introduced in Linux 3.3

This library provides the APIs to open a ALSA compressed device and read/write
compressed data like MP3 etc to it.

This also includes a utility command line player (cplay) which demonstrates 
the usage of this API. Currently this contains support for playing the mp3 format

%package -n %{libname_devel}
Summary:	Headers and libraries for %{name} development
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{libname_devel}
Development files for %{name}

%prep
%setup -q

%build
%configure --disable-static
%make_build

%install
%make_install

#Remove libtool archives.
find %{buildroot} -name '*.la' -delete

%check
make check

%files -n %{libname}
%license COPYING
%doc README
%{_libdir}/lib%{name}.so.%{major}{,.*}

%files -n %{libname_devel}
%{_includedir}/tinycompress*
%{_libdir}/*.so
%{_libdir}/pkgconfig/tinycompress.pc

%files
%{_bindir}/cplay
%{_bindir}/crecord
