Summary:	XView
Summary(pl):	XView
Name:		xview
Version:	3.2p1
Release:	1
License:	GPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(pl):	X11/Biblioteki
Source0:	ftp://sunsite.unc.edu/pub/X11/contrib/libraries/%name%version-X11R6.tar.gz
Patch0:		%{name}-config.patch
#BuildRequires:	
#Requires:	
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description

%description -l pl

%package devel
Summary:	XView devel	
Summary(pl):	Xview devel
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki

%description devel

%description -l pl devel

%prep
%setup -q

%patch

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
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
#%attr(,,)

# optional package

%files devel
%defattr(644,root,root,755)
%doc
#%attr(,,)
#end of optional package
