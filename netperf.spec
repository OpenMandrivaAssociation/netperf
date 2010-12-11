%define name netperf
%define version 2.4.5
%define release %mkrel 2

Summary:	Performance testing tool for TCP/UDP
Name:		%name
Version:	%version
Release:	%release
License:	BSD
Group:		Networking/Other
URL:		http://www.netperf.org/netperf/NetperfPage.html 
Source:		ftp://ftp.netperf.org/netperf/%name-%version.tar.bz2
Patch0:		netperf-2.4.4-add-missing-info-dir-section.patch
Patch1:		netperf-2.4.5-gcc-fix.patch
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
%patch0 -p1 -b .dir-section
%patch1 -p1 -b .gcc

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
