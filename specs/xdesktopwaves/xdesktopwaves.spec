# $Id$
# Authority: matthias

Summary: Set the background of your X Windows desktop under water
Name: xdesktopwaves
Version: 1.0
Release: 1
License: GPL
Group: Amusements/Graphics
URL: http://xdesktopwaves.sourceforge.net/
Source: http://dl.sf.net/xdesktopwaves/xdesktopwaves-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: XFree86-devel
ExclusiveArch: i386

%description
xdesktopwaves is a cellular automata setting the background of your X Windows
desktop under water. Windows and mouse are like ships on the sea. Each movement
of these ends up in moving water waves. You can even have rain and/or storm
stirring up the water.


%prep
%setup


%build
%{__make} %{?_smp_mflags}


%install
%{__mkdir_p} %{buildroot}{%{_bindir},%{_mandir}/man1}
%{__make} install \
    BINDIR=%{buildroot}%{_bindir} \
    MAN1DIR=%{buildroot}%{_mandir}/man1


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc COPYING README
%{_bindir}/xdesktopwaves
%{_mandir}/man1/xdesktopwaves.1*


%changelog
* Fri Nov 19 2004 Matthias Saou <http://freshrpms.net/> 1.0-1
- Initial RPM release.

