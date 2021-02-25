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
# (tpg) https://github.com/akheron/jansson/pull/573
Patch0:		0000-use-version-script-in-case-of-linkers-that-does-not-.patch
Patch1:		0001-cmake-determine-arch-and-set-libdir.patch
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
%cmake \
	-DJANSSON_BUILD_SHARED_LIBS=ON \
	-DJANSSON_INSTALL_LIB_DIR="%{_libdir}" \
	-G Ninja

%ninja_build

# (tpg) 2021-02-25 somehow all tests on ABF fails
# but on local build everythig passes
#check
#ninja_test -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/*.so*

%files -n %{devname}
%doc LICENSE CHANGES
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}
%{_includedir}/*
