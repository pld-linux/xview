
%define		xview_ver	3.2p1.4

Summary:	XView libraries for X11
Summary(pl):	Biblioteki XView dla X11
Name:		xview
Version:	%{xview_ver}
Release:	3
License:	GPL
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Source0:	%{name}_%{version}.orig.tar.gz
Patch0:		%{name}_%{version}-14.diff.gz
#original:
#Source0:	ftp://sunsite.unc.edu/pub/Linux/libs/X/xview/xview-3.2p1.4.src.tar.gz
BuildRequires:	XFree86-devel
Icon:		xv.xpm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

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
XView dostarcza zestaw obiektÛw interfejsu uøytkownika takich jak
scrollbary, menu, panele kontrolne. Zachowanie i funkcjonalno∂Ê tych
obiektÛw jest zgodna ze specyfikacj± OPEN LOOK GUI.

XView to implementacja Suna standardu OpenLook. Pomimo wieku i
wyparcia przez Motifa czy gtk, jest nadal uøyteczna, zw≥aszcza do
zapewnienia kompatybilno∂ci ze starymi programami.

%package devel
Summary:	Header files for XView development
Summary(pl):	Pliki nag≥Ûwkowe XView
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
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
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description static
Static libraries for XView development

%description static -l pl
Biblioteki statyczne XView

%package examples
Summary:	A number of example programs and tutorials for the XView libraries
Summary(pl):	Przyk≥adowe programy i dokumentacja do bibliotek XView
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description examples
Sample programs - with source code - that cover the basics of XView
programming are included in this package.

Also includes documents on the XView API (Application Programming
Interface).

%description examples -l pl
Przyk≥adowe programy - wraz z kodem ºrÛd≥owym - pokazuj±ce podstawy
programowania z uøyciem XView. Pakiet zawiera teø dokumentacjÍ API
XView.

%prep
%setup -q
%patch -p1

%build
rm -f make
# now macro version shows 4.1 - olvm version, must use another macro - xview_ver
IMAKEINCLUDE="-I$RPM_BUILD_DIR/%{name}-%{xview_ver}/config -I%{_libdir}/X11/config"
export IMAKEINCLUDE
cd config
imake -DUseInstalled
cd ..
xmkmf -a
%{__make} CCOPTIONS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}
for name in olgx xview; do
	cp lib/lib$name/lib$name.a $RPM_BUILD_ROOT%{_libdir}
	cp -d lib/lib$name/lib$name.so.* $RPM_BUILD_ROOT%{_libdir}
done

install -d $RPM_BUILD_ROOT%{_mandir}/man7
install xview.man $RPM_BUILD_ROOT%{_mandir}/man7/xview.7

install -d $RPM_BUILD_ROOT%{_includedir}
for dir in olgx olgx_private xview xview_private pixrect; do
	cp -aL build/include/$dir $RPM_BUILD_ROOT%{_includedir}
done

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -ar contrib/examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean 
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libolgx.so.*
%attr(755,root,root) %{_libdir}/libxview.so.*
	  
%files devel
%defattr(644,root,root,755)
%{_mandir}/man7/xview.7.*
%{_includedir}/olgx/*.h
%{_includedir}/olgx_private/*.h
%{_includedir}/pixrect/*.h
%{_includedir}/xview/*.h
%{_includedir}/xview_private/*.h

%files static
%{_libdir}/libolgx.a
%{_libdir}/libxview.a

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
