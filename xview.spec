Summary:	XView libraries for X11
Name:		xview
Version:	3.2p1.4
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	%{name}_%{version}.orig.tar.bz2
Patch0:		%{name}_%{version}-13.diff.bz2
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix /usr/X11R6

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


%package clients
Summary:	OpenWindows clients.
Group:		X11/Window Managers
Requires:	%{name} = %{version}

%description clients
A number of clients and utilties for OpenWindows : clock, textedit,
cmdtool, shelltool, owplaces and props.


%package devel
Summary:	Header files and static libraries for XView development
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}

%description devel
All the files needed to develop applications that, using the XView
libraries, meet the Open Look interface specifications.


%package examples
Summary:	A number of example programs and tutorials for the XView libraries.
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel

%description examples
Sample programs - with source code - that cover the basics of XView
programming are included in this package.

Also includes documents on the XView API (Application Programming
Interface).


%package -n olwm
Summary:	OpenLook Window Manager
Group:		X11/Window Managers
Requires:	xview = %{version}

%description -n olwm
This package contains the traditional Open Look Window Manager. For an
extended version that offers virtual desktops, have a look at the
package olvwm.

%package -n olvwm
Summary:	OpenLook Virtual Window Manager
Version:	4.1
Group:		X11/Window Managers
Requires:	xview = %{version}

%description -n olvwm
This package contains an extended version of olwm, the original
OpenLook window manager, enhanced for handling of virtual desktops
with support for 24-bit color modes.

%prep
%setup -q
%patch -p1 -b .orig
%build
rm -f make
IMAKEINCLUDE="-I$RPM_BUILD_DIR/%name-%version/config -I%{_libdir}/X11/config"
export IMAKEINCLUDE
cd config
imake -DUseInstalled $IMAKEINCLUDE
cd ..
xmkmf -a
%{__make} RPM_OPT_FLAGS="%{rpmcflags}" World

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_bindir},%{_datadir}}

%{__make} DESTDIR=$RPM_BUILD_ROOT install

mv -f $RPM_BUILD_ROOT%{_libdir}/help/clock.info.keep $RPM_BUILD_ROOT%{_libdir}/help/clock.info

for prog in capitalize insert_brackets remove_brackets shift_lines; do \
	  install -m555 contrib/misc/$prog   $RPM_BUILD_ROOT%{_bindir}; \
	  pwd; \
	  install -m555 contrib/misc/$prog.1 $RPM_BUILD_ROOT%{_mandir}/man1; \
done
	
install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/xview/

for file in text_extras_menu textswrc ttyswrc; do \
	mv $RPM_BUILD_ROOT%{_libdir}/.$file $RPM_BUILD_ROOT%{_sysconfdir}/X11/xview/$file; \
	ln -fs %{_sysconfdir}/X11/xview/$file $RPM_BUILD_ROOT%{_libdir}/.$file; \
done
	
install -d $RPM_BUILD_ROOT%{_mandir}/man7
mv $RPM_BUILD_ROOT%{_mandir}/man1/xview.1x $RPM_BUILD_ROOT%{_mandir}/man7/xview.7x

install contrib/misc/owplaces $RPM_BUILD_ROOT%{_bindir}
install contrib/misc/openwin  $RPM_BUILD_ROOT%{_bindir}

for file in clock cmdtool shelltool textedit; do \
	  mv $RPM_BUILD_ROOT%{_mandir}/man1/$file.1x $RPM_BUILD_ROOT%{_mandir}/man1/$file.1; \
done

install -D contrib/misc/props-locale.C $RPM_BUILD_ROOT%{_datadir}/locale/C/props/C
install -D contrib/misc/props-locale.basic_setting $RPM_BUILD_ROOT%{_datadir}/locale/C/props/basic_setting

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install $RPM_BUILD_ROOT%{_datadir}/src/xview/examples/bin/* $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}
	
for file in olwm olwmslave; do \
	mv $RPM_BUILD_ROOT%{_mandir}/man1/$file.1x $RPM_BUILD_ROOT%{_mandir}/man1/$file.1; \
done

for file in olvwm olvwmrc; do \
	  mv $RPM_BUILD_ROOT%{_mandir}/man1/$file.1x $RPM_BUILD_ROOT%{_mandir}/man1/$file.1; \
done

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/capitalize
%attr(755,root,root) %{_bindir}/insert_brackets
%attr(755,root,root) %{_bindir}/remove_brackets
%attr(755,root,root) %{_bindir}/shift_lines
%{_libdir}/text_extras_menu
%{_libdir}/textswrc
%{_libdir}/ttyswrc
%{_libdir}/.text_extras_menu
%{_libdir}/.textswrc
%{_libdir}/.ttyswrc
%{_sysconfdir}/X11/xview/text_extras_menu
%{_sysconfdir}/X11/xview/textswrc
%{_sysconfdir}/X11/xview/ttyswrc
%{_prefix}/openwin
%{_mandir}/man1/capitalize.*
%{_mandir}/man1/insert_brackets.*
%{_mandir}/man1/remove_brackets.*
%{_mandir}/man1/shift_lines.*
%{_mandir}/man7/xview.7x.*
%attr(755,root,root) %{_libdir}/libolgx.so.*
%attr(755,root,root) %{_libdir}/libxview.so.*
%attr(755,root,root) %{_includedir}/bitmaps/*
%{_includedir}/images/*
%{_libdir}/help/textsw.info
%{_libdir}/help/ttysw.info
%{_libdir}/help/xview.info
	  
%files devel
%defattr(644,root,root,755)
%config %{_prefix}/X11R6/lib/X11/config
%{_includedir}/olgx/*.h
%{_includedir}/olgx_private/*.h
%{_includedir}/pixrect/*.h
%{_includedir}/xview/*.h
%{_includedir}/xview_private/*.h
%{_libdir}/libolgx.a
%{_libdir}/libxview.a

%files clients
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/clock
%attr(755,root,root) %{_bindir}/cmdtool
%attr(755,root,root) %{_bindir}/shelltool
%attr(755,root,root) %{_bindir}/props
%attr(755,root,root) %{_bindir}/textedit
%attr(755,root,root) %{_bindir}/owplaces
%attr(755,root,root) %{_bindir}/openwin
%{_mandir}/man1/clock.*
%{_mandir}/man1/cmdtool.*
%{_mandir}/man1/shelltool.*
%{_mandir}/man1/textedit.*
%{_datadir}/locale/C/props/C
%{_datadir}/locale/C/props/basic_setting

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files -n olwm
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/olwm*
%{_mandir}/man1/olwm*
%{_libdir}/help/olwm.info
%{_libdir}/help/workspace.info

%files -n olvwm
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/olvwm*
%{_mandir}/man1/olvwm*
%{_libdir}/help/olvwm.info
