%define altname nurgle
%define verdate 2009-03-17

Summary:	Arnold - Amstrad CPC emulator
Name:		arnold
Version:	0.%(sed -e 's/-//g' <<<%{verdate})
Release:	6
License:	GPLv2+
#except amstrad roms
Group:		Emulators
Url:		http://arnold.berlios.de/
Source0:	http://download.berlios.de/%{name}/%{name}-%{altname}-%{verdate}.tar.bz2
Source1:	%{name}-32.png
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(gtk+-2.0)

%description
Arnold "Nurgle" is an Amstrad CPC emulator for Linux.
It is based on original Arnold from Kevin Thacker.
It emulates from CPC 464 to CPC 6128+.

%files
%doc ../README.FIRST ../gpl-spanish.htm ../*.txt ../*.linux ../docs/* ../extras/*
%attr(0755,root,games) %{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}
%{_iconsdir}/*
%{_datadir}/applications/mandriva-%{name}.desktop

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}/src

%build
%configure2_5x
%make

%install
#makeinstall
install -d -m 0755 %{buildroot}/%{_gamesbindir}
install -m 0755 ../%{name} %{buildroot}%{_gamesbindir}

install -d -m 0755 %{buildroot}/%{_gamesdatadir}/%{name}/roms/ARNOR/
install -m 0644 roms/ARNOR/* %{buildroot}/%{_gamesdatadir}/%{name}/roms/ARNOR/

#icon
install -d -m 755 %{buildroot}%{_iconsdir}
install -m 644 %{SOURCE1} %{buildroot}%{_iconsdir}/%{name}.png

#xdg menu
install -d -m 755 %{buildroot}%{_datadir}/applications
cat<<EOF>%{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Encoding=UTF-8
Name=Arnold
Comment=Amstrad CPC emulator
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;Emulator;
EOF

