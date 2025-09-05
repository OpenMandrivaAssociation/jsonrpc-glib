%global api 1.0
%global major 1
%define libname %mklibname jsonrpc_glib %{api} %{major}
%define girname %mklibname jsonrpc-gir %{api}
%define devname %mklibname -d jsonrpc_glib %{api}

%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:           jsonrpc-glib
Version:	3.44.2
Release:	2
Summary:        A JSON-RPC library for GLib
Group:		System/Libraries

License:        LGPLv2+
URL:            https://git.gnome.org/browse/jsonrpc-glib/
Source0:        https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  python-six 

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(vapigen)

%description
Jsonrpc-GLib is a JSON-RPC library for GLib. It includes support for
communicating as both a JSON-RPC client and server. Additionally,
supports upgrading connections to use GVariant for less runtime overhead.

%package        -n %libname
Summary:        Development files for %{name}
Group:		System/Libraries
Obsoletes:	%{_lib}jsonrpc_glib0 < 3.26.1-2

%description    -n %libname
Jsonrpc-GLib is a JSON-RPC library for GLib. It includes support for
communicating as both a JSON-RPC client and server. Additionally,
supports upgrading connections to use GVariant for less runtime overhead.

%package	-n %girname
Summary:	GObject Introspection interface description for Jsonrpc
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}
Conflicts:	%{_lib}jsonrpc-glib0 < 3.26.1-2

%description	-n %girname
GObject Introspection interface description for Jsonrpc.

%package        -n %devname
Summary:        Development files for %{name}
Requires:       %{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{name}%{api}-devel = %{version}-%{release}
Obsoletes:	%{_lib}jsonrpc_glib-devel < 3.26.1-2

%description    -n %devname
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%build
%meson -D enable_gtk_doc=true
%meson_build


%install
%meson_install


%check
#meson_test

%files -n %libname
%license COPYING
%doc AUTHORS
%{_libdir}/libjsonrpc-glib-%{api}.so.%{major}{,.*}

%files -n %girname
%{_libdir}/girepository-1.0/Jsonrpc-%{api}.typelib

%files -n %devname
%doc CONTRIBUTING.md
%doc %{_datadir}//doc/jsonrpc-glib/
%{_datadir}/gir-1.0/Jsonrpc-%{api}.gir
%{_datadir}/vala/vapi/jsonrpc-glib-%{api}.*
%{_includedir}/jsonrpc-glib-%{api}/
%{_libdir}/libjsonrpc-glib-%{api}.so
%{_libdir}/pkgconfig/jsonrpc-glib-%{api}.pc
