%define		packagename	lineak_defaultplugin

Summary:	This is the default plugin for the lineakd daemon
Summary(pl):	To jest domy¶lna wtyczka demona lineakd
Name:		lineak-defaultplugin
Version:	0.8.4
Release:	0.9
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/lineak/%{packagename}-%{version}.tar.gz
# Source0-md5:	336b4fa5aa40b1166c2aa5418740357b
Patch0:		%{name}-DESTDIR.patch
URL:		http://lineak.sourceforge.net/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	lineakd >= %{version}
Requires:	lineakd >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a set of plugins for lineakd. The plugins allow binding
actions to special keys. This plugin contains the original lineakd
macros:

EAK_MUTE
EAK_VOLUP
EAK_VOLDOWN
EAK_PCM_UP
EAK_PCM_DOWN
EAK_PCM_MUTE
EAK_EJECT
EAK_OPEN_TRAY_SCSI
EAK_OPEN_TRAY
EAK_CLOSE_TRAY
EAK_SENDKEYS or EAK_SYM
EAK_SENDKEYS_ROOT
EAK_MEDIADETECT

%description -l pl
To jest zbiór wtyczek do lineakd. Wtyczki te pozwalaj± na dowi±zywanie
akcji do specjalnych klawiszy. Ten plugin zawiera pierwotne makra
lineakd:

EAK_MUTE
EAK_VOLUP
EAK_VOLDOWN
EAK_PCM_UP
EAK_PCM_DOWN
EAK_PCM_MUTE
EAK_EJECT
EAK_OPEN_TRAY_SCSI
EAK_OPEN_TRAY
EAK_CLOSE_TRAY
EAK_SENDKEYS or EAK_SYM
EAK_SENDKEYS_ROOT
EAK_MEDIADETECT

%prep
%setup -q -n %{packagename}-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README TODO media-detect.conf
%{_libdir}/lineakd/plugins/*
%{_sysconfdir}/*
%{_mandir}/man*/*
