# $Id: $

# Authority: dries
# Upstream: 

Summary: Real-time strategy game
Name: boson
Version: 0.10
Release: 1
License: GPL
Group: Amusements/Games
URL: http://boson.eu.org/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/boson/boson-all-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: 

%description
Boson is an OpenGL real-time strategy game, with the feeling of
Command&Conquer(tm) or StarCraft(tm). It is designed to run on Unix (Linux)
computers, and is built on top of the KDE, Qt and kdegames libraries.
A minimum of two players is required, since there is no artificial
intelligence yet.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Name Thingy Tool
Comment=Do things with things
Icon=name.png
Exec=name
Terminal=false
Type=Application
StartupNotify=true
Encoding=UTF-8
Categories=Application;Network;X-Red-Hat-Extra;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING CREDITS INSTALL LICENSE NEWS README THANKS TODO
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Mon May 3 2004 Dries Verachtert <dries@ulyssis.org> 0.10-1 
- Initial package.

