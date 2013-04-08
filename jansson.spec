%define major	4
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Name:		jansson
Version:	2.4
Release:	1
Summary:	C library for encoding, decoding and manipulating JSON data
Group:		Development/C 
License:	MIT
URL:		http://www.digip.org/jansson/
Source0:	http://www.digip.org/jansson/releases/jansson-%{version}.tar.bz2

BuildRequires: python-sphinx


%description
Small library for parsing and writing JSON documents.

%package -n %{libname}
Summary: Libraries for encoding, decoding and manipulating JSON data
Group: System/Libraries

%description -n %{libname}
C library for encoding, decoding and manipulating JSON data

%package -n	%{devname}
Summary:	Header files for jansson
Group:		Development/C 
Requires:	%{name} = %{version}-%{release}

%description -n %{devname}
Header files for developing applications making use of jansson.

%prep
%setup -q

%build
autoreconf -v --install
%configure --disable-static
%make
make html

%check
make check

%install
make install INSTALL="install -p" DESTDIR="$RPM_BUILD_ROOT"
rm "$RPM_BUILD_ROOT%{_libdir}"/*.la


%files -n %{libname}
%{_libdir}/*.so.*

%files -n %{devname}
%doc LICENSE CHANGES
%doc doc/_build/html/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/*


%changelog
* Sat May 05 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.3.1-1
+ Revision: 796627
- version update 2.3.1

* Sat Nov 05 2011 Alexander Khrukin <akhrukin@mandriva.org> 2.2.1-1
+ Revision: 721550
- imported package jansson

