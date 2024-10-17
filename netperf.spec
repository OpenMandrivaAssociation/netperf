%define name netperf
%define version 2.6.0
%define release  3

Summary:	Performance testing tool for TCP/UDP
Name:		%name
Version:	%version
Release:	%release
License:	BSD
Group:		Networking/Other
URL:		https://www.netperf.org/netperf/NetperfPage.html 
Source0:	ftp://ftp.netperf.org/netperf/%name-%version.tar.bz2

%description
Netperf is a benchmark that can be used to measure the performance 
of many different types of networking. It provides tests for both 
unidirecitonal throughput, and end-to-end latency.

The environments currently measureable by netperf include:

* TCP and UDP via BSD Sockets for both IPv4 and IPv6
* DLPI
* Unix Domain Sockets
* SCTP for both IPv4 and IPv6 

%prep
%setup -q 

%build
%configure2_5x \
	--enable-unixdomain \
	--enable-sdp \
	--enable-exs \
	--enable-sctp
%make 

%install
%makeinstall_std




%files
%doc README AUTHORS COPYING Release_Notes
%{_bindir}/netperf
%{_bindir}/netserver
%{_infodir}/netperf.*
%{_mandir}/man1/netperf.1*
%{_mandir}/man1/netserver.1*


%changelog
* Thu Jun 28 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.6.0-1
+ Revision: 807376
- version update 2.6.0

* Wed Jul 20 2011 Bruno Cornec <bcornec@mandriva.org> 2.5.0-1
+ Revision: 690746
- Add upstream sources 2.5.0
- Update to upstream netperf 2.5.0

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.0 packages

* Sun Jul 12 2009 Bruno Cornec <bcornec@mandriva.org> 2.4.5-1mdv2010.0
+ Revision: 394969
- Update to upstream 2.4.5 and fix compiler errors on fprintf format (reported upstrem)
- Update netperf to 2.4.5 and fix compiler issues (reported upstream)

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - fix info file

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Oct 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.4.4-1mdv2008.1
+ Revision: 100087
- new version
- spec file clean

