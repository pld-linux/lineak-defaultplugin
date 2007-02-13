Summary:	The default plugin for the lineakd daemon
Summary(pl.UTF-8):	Domyślna wtyczka demona lineakd
Name:		lineak-defaultplugin
Version:	0.9
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://dl.sourceforge.net/lineak/%{name}-%{version}.tar.gz
# Source0-md5:	425df8c225c1a079a4ed1f221d2a5479
Patch0:		%{name}-make.patch
URL:		http://lineak.sourceforge.net/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	lineakd-devel >= 0.9
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libX11-devel
Requires:	lineakd >= 0.9
Obsoletes:	lineak_defaultplugin
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a plugin for lineakd. The plugin allows binding actions to
special keys.

This plugin contains the original lineakd macros:

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

%description -l pl.UTF-8
To jest wtyczka do lineakd. Wtyczka ta pozwala na dowiązywanie akcji
do specjalnych klawiszy.

Ta wtyczka zawiera pierwotne makra lineakd:

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
%setup -q
%patch0 -p1

# kill plugin dir existence test
sed -i -e 's/test ! -d \$pdir/false/' admin/lineak.m4.in
cat admin/{acinclude.m4.in,lineak.m4.in} > acinclude.m4

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure \
	--with-lineak-plugindir=%{_libdir}/lineakd/plugins

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/lineakd/plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO media-detect.conf
%attr(755,root,root) %{_libdir}/lineakd/plugins/defaultplugin.so
%attr(755,root,root) %{_libdir}/lineakd/plugins/mediadetectplugin.so
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/media-detect.conf
%{_mandir}/man1/lineak_defaultplugin.1*
