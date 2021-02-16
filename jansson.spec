%define major 4
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	C library for encoding, decoding and manipulating JSON data
Name:		jansson
Version:	2.13.1
Release:	4
Group:		Development/C
License:	MIT
Url:		http://www.digip.org/jansson/
Source0:	http://www.digip.org/jansson/releases/%{name}-%{version}.tar.bz2
# (tpg) https://github.com/akheron/jansson/issues/523
Patch0:		0000-build-Add-a-symbol-version-to-all-exported-symbols-f.patch
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	python-sphinx

%description
Small library for parsing and writing JSON documents.

%package -n %{libname}
Summary:	Libraries for encoding, decoding and manipulating JSON data
Group:		System/Libraries

%description -n %{libname}
C library for encoding, decoding and manipulating JSON data

%package -n %{devname}
Summary:	Header files for jansson
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Header files for developing applications making use of jansson.

%prep
%autosetup -p1

%build
%cmake -G Ninja
%ninja_build

%check
%ninja_test

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/libjansson.so.%{major}*

%files -n %{devname}
%doc LICENSE CHANGES
#% doc doc/_build/html/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/*
