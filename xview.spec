Summary:	XView
Summary(pl):	XView
Name:		xview
Version:	3.2p1
Release:	1
Copyright:	GPL
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Source:		ftp://sunsite.unc.edu/pub/X11/contrib/libraries/%name%version-X11R6.tar.gz
Patch:		xview-config.patch
#BuildRequires:	
#Requires:	
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr/X11R6

%description

%description -l pl
 # optional package =====================

%package devel
Summary:	XView devel	
Summary(pl):	Xview devel
Group:		XXX
Group(pl):	XXX

%description devel

%description -l pl devel
 # end of optional package ==============

%prep
%setup -q

%patch

%build
rm make
IMAKEINCLUDE="-I$RPM_BUILD_DIR/%name-%version/config -I/usr/X11R6/lib/X11/config"
export IMAKEINCLUDE
cd config
imake -DUseInstalled $IMAKEINCLUDE
cd ..
xmkmf -a
%{__make} RPM_OPT_FLAGS="$RPM_OPT_FLAGS" World

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
