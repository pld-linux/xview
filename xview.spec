
%define		xview_ver	3.2p1.4

Summary:	XView libraries for X11
Summary(pl):	Biblioteki XView dla X11
Name:		xview
Version:	%{xview_ver}
Release:	6
License:	GPL
Group:		Development/Libraries
Source0:	ftp://step.polymtl.ca/pub/Xview/libs/xview/Xview-%{version}/%{name}-%{version}.src.tar.gz
# Source0-md5:	b9ff26d6ad378af320bac45154ceaeba
# http://ftp.debian.org/debian/pool/main/x/xview/
Patch0:		%{name}_%{version}-17.diff.gz
URL:		http://step.polymtl.ca/~coyote/xview_main.html
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
XView provides a set of pre-built, user-interface objects such as
canvases, scrollbars, menus, and control panels. The appearance and
functionality of these objects follow the OPEN LOOK Graphical User
Interface (GUI) specification.

This is the Sun implementation of the OpenLook interface standard,
using the xview libraries. While somewhat outdated and superseded by
Motif, or gtk, it is still very useful, especially in providing
compatibility with older installations.

It is possible that the openwin desktop takes up much less disk space
to install and memory to run than modern desktops, which would make it
a good candidate for old hardware.

%description -l pl
XView dostarcza zestaw obiektów interfejsu u¿ytkownika takich jak
scrollbary, menu, panele kontrolne. Zachowanie i funkcjonalno¶æ tych
obiektów jest zgodna ze specyfikacj± OPEN LOOK GUI.

XView to implementacja Suna standardu OpenLook. Pomimo wieku i
wyparcia przez Motifa czy gtk, jest nadal u¿yteczna, zw³aszcza do
zapewnienia kompatybilno¶ci ze starymi programami.

%package devel
Summary:	Header files for XView development
Summary(pl):	Pliki nag³ówkowe XView
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
All the files needed to develop applications that, using the XView
libraries, meet the OpenLook interface specifications.

%description devel -l pl
Wszystko co potrzebne do tworzenia aplikacji korzystaj±cych z
bibliotek XView, zgodnych ze specyfikacj± interfejsu OpenLook.

%package static
Summary:	Static libraries for XView development
Summary(pl):	Biblioteki statyczne XView
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description static
Static libraries for XView development

%description static -l pl
Biblioteki statyczne XView

%package examples
Summary:	A number of example programs and tutorials for the XView libraries
Summary(pl):	Przyk³adowe programy i dokumentacja do bibliotek XView
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description examples
Sample programs - with source code - that cover the basics of XView
programming are included in this package.

Also includes documents on the XView API (Application Programming
Interface).

%description examples -l pl
Przyk³adowe programy - wraz z kodem ¼ród³owym - pokazuj±ce podstawy
programowania z u¿yciem XView. Pakiet zawiera te¿ dokumentacjê API
XView.

%prep
%setup -q
%patch0 -p1

%build
rm -f make
# now macro version shows 4.1 - olvm version, must use another macro - xview_ver
IMAKEINCLUDE="-I$RPM_BUILD_DIR/%{name}-%{xview_ver}/config -I%{_prefix}/X11R6/lib/X11/config"
export IMAKEINCLUDE
cd config
imake -DUseInstalled
cd ..
xmkmf -a
%{__make} \
	CC=%{__cc} \
	CCOPTIONS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_mandir}/man7,%{_includedir},%{_examplesdir}/%{name}-%{version}}

for name in olgx xview; do
	cp lib/lib$name/lib$name.a $RPM_BUILD_ROOT%{_libdir}
	cp -d lib/lib$name/lib$name.so.* $RPM_BUILD_ROOT%{_libdir}
done

install xview.man $RPM_BUILD_ROOT%{_mandir}/man7/xview.7

for dir in olgx olgx_private xview xview_private pixrect; do
	cp -aL build/include/$dir $RPM_BUILD_ROOT%{_includedir}
done

ln -sf libolgx.so.3.2.4 $RPM_BUILD_ROOT%{_libdir}/libolgx.so
ln -sf libxview.so.3.2.4 $RPM_BUILD_ROOT%{_libdir}/libxview.so

cp -ar contrib/examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libolgx.so.*.*
%attr(755,root,root) %{_libdir}/libxview.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libolgx.so
%attr(755,root,root) %{_libdir}/libxview.so
%{_mandir}/man7/xview.7.*
%{_includedir}/olgx
%{_includedir}/olgx_private
%{_includedir}/pixrect
%{_includedir}/xview
%{_includedir}/xview_private

%files static
%defattr(644,root,root,755)
%{_libdir}/libolgx.a
%{_libdir}/libxview.a

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
