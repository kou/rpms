# $Id$
# Authority: dag
# Upstream: Anthony Tekatch <anthony$unihedron,com>

%{?dist: %{expand: %%define %dist 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

Summary: Units conversion utility
Name: gonvert
Version: 0.2.11
Release: 1
License: GPL
Group: Applications/Engineering
URL: http://unihedron.com/projects/gonvert/gonvert.php

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.unihedron.com/projects/gonvert/downloads/gonvert-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python >= 1.5, pygtk2-devel >= 2.0, libglade >= 0.13, gnome-libs >= 1.2.4
Requires: python >= 1.5, pygtk2 >= 2.0, libglade >= 0.13, gnome-libs >= 1.2.4
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%description
gonvert is a conversion utility that allows conversion between many units 
like CGS, Ancient, Imperial with many categories like length, mass, numbers, 
etc. All units converted values shown at once as you type. Easy to add/change 
your own units.

%prep 
%setup

%build 
%{__make} %{?_smp_mflags}

%install 
%{__rm} -rf %{buildroot}
%makeinstall

%if %{!?_without_freedesktop:1}0
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor gnome --delete-original \
		--dir %{buildroot}%{_datadir}/applications    \
		--add-category X-Red-Hat-Base                 \
		%{buildroot}%{_datadir}/gnome/apps/Utilities/gonvert.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(-, root, root, 0755) 
%doc doc/*
%{_bindir}/gonvert
%{_datadir}/gonvert/
%{!?_without_freedesktop:%{_datadir}/applications/gnome-gonvert.desktop}
%{?_without_freedesktop:%{_datadir}/gnome/apps/Utilities/gonvert.desktop}
%{_datadir}/pixmaps/*.png
%exclude %{_docdir}/gonvert/

%changelog 
* Sat Nov 20 2004 Dag Wieers <dag@wieers.com> - 0.2.11-1
- Updated to release 0.2.11.

* Thu Jun 24 2004 Dag Wieers <dag@wieers.com> - 0.2.04-1
- Updated to release 0.2.04.

* Wed Jun 23 2004 Dag Wieers <dag@wieers.com> - 0.2.03-1
- Updated to release 0.2.03.

* Tue Jun 22 2004 Dag Wieers <dag@wieers.com> - 0.2.02-1
- Updated to release 0.2.02.

* Mon Jun 21 2004 Dag Wieers <dag@wieers.com> - 0.2.01-1
- Updated to release 0.2.01.

* Tue Apr 06 2004 Dag Wieers <dag@wieers.com> - 0.1.10-2
- Small cosmetic changes.

* Sat Mar 13 2004 Dag Wieers <dag@wieers.com> - 0.1.10-1
- Updated to release 0.1.10.

* Tue Feb 03 2004 Dag Wieers <dag@wieers.com> - 0.1.7-1
- Swapped pygtk requirement by pygtk2. (Paolo Dona)

* Mon Jan 26 2004 Dag Wieers <dag@wieers.com> - 0.1.7-0
- Updated to release 0.1.7.

* Sat Jun 29 2003 Dag Wieers <dag@wieers.com> - 0.1.6-0
- Updated to release 0.1.6.

* Wed Feb 26 2003 Dag Wieers <dag@wieers.com> - 0.1.5-0
- Initial package. (using DAR)
