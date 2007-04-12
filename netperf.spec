%define name netperf
%define version 2.4.2
%define release %mkrel 2
Name: %name
Version: %version
Summary: Performance testing tool for TCP/UDP
Release: %release
License: BSD
Group: Networking/Other
Source: ftp://ftp.cup.hp.com/dist/networking/benchmarks/netperf/%name-%version.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-root
URL: http://www.netperf.org/netperf/NetperfPage.html 

%description
Netperf is a tool for measure TCP/UDP speeds

%prep
%setup -q 

%build
%configure
%make 

%install
rm -rf $RPM_BUILDROOT
%makeinstall

%clean
rm -rf $RPM_BUILDROOT

%preun
%_remove_install_info %{name}.info

%post
%_install_info %{name}.info

%files
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_bindir}/netperf
%attr(0755,root,root) %{_bindir}/netserver
%{_infodir}/netperf.*
%{_mandir}/man1/netperf.1*
%{_mandir}/man1/netserver.1*

%doc README
%doc COPYING
%doc Release_Notes


