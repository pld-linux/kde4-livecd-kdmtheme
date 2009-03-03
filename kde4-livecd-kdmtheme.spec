
Summary:	PLD-LiveCD KDE4 KDM Theme
Summary(pl.UTF-8):	Motyw KDM do PLD-LiveCD z KDE4
Name:		kde4-livecd-kdmtheme
Version:	0
Release:	1
License:	LGPLv3
Group:		X11/Libraries
Source0:	%{name}.tar.gz
# Source0-md5:	b3af6f399711552f526458b28deb157a
URL:		http://livecd.pld-linux.pl
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLD-LiveCD KDE4 KDM Theme.

%description -l pl.UTF-8
Motyw KDM do PLD-LiveCD z KDE4.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/apps/kdm/themes
cp -ar LiveCD $RPM_BUILD_ROOT%{_datadir}/apps/kdm/themes/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/kdm/themes/LiveCD
