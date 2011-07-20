%define name netperf
%define version 2.5.0
%define release %mkrel 1

Summary:	Performance testing tool for TCP/UDP
Name:		%name
Version:	%version
Release:	%release
License:	BSD
Group:		Networking/Other
URL:		http://www.netperf.org/netperf/NetperfPage.html 
Source:		ftp://ftp.netperf.org/netperf/%name-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

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
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%preun
%_remove_install_info %{name}.info

%post
%_install_info %{name}.info

%postun
%_remove_install_info %{name}.info

%files
%defattr(-,root,root)
%doc README AUTHORS COPYING Release_Notes
%{_bindir}/netperf
%{_bindir}/netserver
%{_infodir}/netperf.*
%{_mandir}/man1/netperf.1*
%{_mandir}/man1/netserver.1*
