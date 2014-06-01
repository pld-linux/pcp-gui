# NOTE: since pcp 3.9.4 pcp-gui is integrated into main pcp sources
Summary:	Performance Co-Pilot GUI tools
Summary(pl.UTF-8):	Performance Co-Pilot - narzędzia GUI
Name:		pcp-gui
Version:	1.5.13
Release:	1.1
License:	LGPL v2.1 (libraries), GPL v2 (the rest)
Group:		X11/Applications
Source0:	ftp://oss.sgi.com/projects/pcp/download/%{name}-%{version}.src.tar.gz
# Source0-md5:	c89224f441039cbf13154e55111395f1
URL:		http://oss.sgi.com/projects/pcp/
BuildRequires:	QtAssistant-compat-devel >= 4
BuildRequires:	QtCore-devel >= 4
BuildRequires:	QtGui-devel >= 4
BuildRequires:	autoconf
BuildRequires:	pcp-devel
BuildRequires:	qt4-build >= 4
BuildRequires:	qt4-qmake >= 4
Requires:	pcp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pmchart is designed to produce stripcharts from Performance Co-Pilot
(PCP) performance metrics fetched from live sources (one or more pmcd
hosts) and also historical sources (one or more PCP archives).

pmtime is a graphical time controller utility that coordinates time
updates and VCR-like playback for other utilities like pmchart and
pmval.

%description -l pl.UTF-8
pmchart służy do tworzenia wykresów z danych o wydajności pakietu PCP
(Performance Co-Pilot) pobranych z żywych źródeł (jednego lub większej
liczby hostów pmcd) oraz źródeł historycznych (jednego lub większej
liczby archiwów PCP).

pmtime to graficzne narzędzie do kontroli czasu, koordynujące
aktualizację czasu oraz odtwarzanie w stylu VCR dla innych narzędzi,
takich jak pmchart czy pmval.

%prep
%setup -q

%build
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DIST_ROOT=$RPM_BUILD_ROOT \
	INSTALL="$(pwd)/install-sh" \
	HAVE_BZIP2ED_MANPAGES=false \
	HAVE_ZIPPED_MANPAGES=false

# could be eventually packaged in examplesdir
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/pcp/demos
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/pcp-gui
%{__mv} $RPM_BUILD_ROOT%{_docdir}/pcp-doc/html html
# tests
%{__rm} -r $RPM_BUILD_ROOT/var/lib/pcp-gui/testsuite

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/{CHANGES,COPYING} html
%attr(755,root,root) %{_bindir}/pmchart
%attr(755,root,root) %{_bindir}/pmconfirm
%attr(755,root,root) %{_bindir}/pmdumptext
%attr(755,root,root) %{_bindir}/pmmessage
%attr(755,root,root) %{_bindir}/pmquery
%attr(755,root,root) %{_bindir}/pmtime
%attr(755,root,root) %{_libdir}/pcp/bin/pmsnap
%dir %{_sysconfdir}/pcp/pmsnap
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pcp/pmsnap/control
%{_desktopdir}/pmchart.desktop
%{_pixmapsdir}/pmchart.png
%{_pixmapsdir}/pmtime.png
%{_mandir}/man1/pmchart.1*
%{_mandir}/man1/pmconfirm.1*
%{_mandir}/man1/pmdumptext.1*
%{_mandir}/man1/pmmessage.1*
%{_mandir}/man1/pmquery.1*
%{_mandir}/man1/pmsnap.1*
%{_mandir}/man1/pmtime.1*
/var/lib/pcp/config/pmafm/pcp-gui
%config(noreplace) %verify(not md5 mtime size) /var/lib/pcp/config/pmchart/CPU
%config(noreplace) %verify(not md5 mtime size) /var/lib/pcp/config/pmchart/ApacheServer
%config(noreplace) %verify(not md5 mtime size) /var/lib/pcp/config/pmchart/Disk
%config(noreplace) %verify(not md5 mtime size) /var/lib/pcp/config/pmchart/Diskbytes
%config(noreplace) %verify(not md5 mtime size) /var/lib/pcp/config/pmchart/ElasticsearchServer
%config(noreplace) %verify(not md5 mtime size) /var/lib/pcp/config/pmchart/Filesystem
%config(noreplace) %verify(not md5 mtime size) /var/lib/pcp/config/pmchart/Loadavg
%config(noreplace) %verify(not md5 mtime size) /var/lib/pcp/config/pmchart/Memory
%config(noreplace) %verify(not md5 mtime size) /var/lib/pcp/config/pmchart/NFS2
%config(noreplace) %verify(not md5 mtime size) /var/lib/pcp/config/pmchart/NFS3
%config(noreplace) %verify(not md5 mtime size) /var/lib/pcp/config/pmchart/Netbytes
%config(noreplace) %verify(not md5 mtime size) /var/lib/pcp/config/pmchart/Netpackets
%config(noreplace) %verify(not md5 mtime size) /var/lib/pcp/config/pmchart/Overview
%config(noreplace) %verify(not md5 mtime size) /var/lib/pcp/config/pmchart/PMCD
%config(noreplace) %verify(not md5 mtime size) /var/lib/pcp/config/pmchart/Paging
%config(noreplace) %verify(not md5 mtime size) /var/lib/pcp/config/pmchart/Schemes
%config(noreplace) %verify(not md5 mtime size) /var/lib/pcp/config/pmchart/Sockets
%config(noreplace) %verify(not md5 mtime size) /var/lib/pcp/config/pmchart/Swap
%config(noreplace) %verify(not md5 mtime size) /var/lib/pcp/config/pmchart/Syscalls
%dir /var/lib/pcp/config/pmsnap
%config(noreplace) %verify(not md5 mtime size) /var/lib/pcp/config/pmsnap/Snap
%config(noreplace) %verify(not md5 mtime size) /var/lib/pcp/config/pmsnap/crontab
%config(noreplace) %verify(not md5 mtime size) /var/lib/pcp/config/pmsnap/summary.html
