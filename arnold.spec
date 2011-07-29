Name:			arnold
%define altname		nurgle
%define verdate		2009-03-17
Version:		0.%(sed -e 's/-//g' <<<%{verdate})
Release:		%mkrel 4

Summary:	Arnold - Amstrad CPC emulator
License:	GPLv2+
#except amstrad roms.
Group:		Emulators
URL:		http://arnold.berlios.de/
Source0:	http://download.berlios.de/%{name}/%{name}-%{altname}-%{verdate}.tar.bz2
Source1:	%{name}-32.png
#Patch0:		%{name}-20081209-plf-string-literal.patch
#Patch1:		%{name}-20081209-plf-fix-linking-with-as-needed.patch
#Patch2:		%{name}-20081209-plf-64bit-dsk.patch
#Patch3:		%{name}-20081209-plf-64bit-cpcplus.patch
#Patch4:		%{name}-20081209-plf-various-warnings.patch

BuildRequires:	SDL-devel
BuildRequires:	gtk2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Arnold "Nurgle" is an Amstrad CPC emulator for Linux.
It is based on original Arnold from Kevin Thacker.
It emulates from CPC 464 to CPC 6128+.

%prep
%setup -q -n %{name}/src
#patch0 -p1 -b .string-literal
#patch1 -p1 -b .as-needed
#patch2 -p1 -b .64-dsk
#patch3 -p1 -b .64-cpc+
#patch4 -p1 -b .gcc-warnings

%build
%configure
%make

%install
rm -rf %{buildroot}
#makeinstall
install -d -m 0755 %{buildroot}/%{_gamesbindir}
install -m 0644 ../%{name} %{buildroot}/%{_gamesbindir}

install -d -m 0755 %{buildroot}/%{_gamesdatadir}/%{name}/roms/ARNOR/
install -m 0644 roms/ARNOR/* %{buildroot}/%{_gamesdatadir}/%{name}/roms/ARNOR/

#icon
install -d -m 755 %{buildroot}%{_iconsdir}
install -m 644 %{SOURCE1} %{buildroot}%{_iconsdir}/

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
Categories=X-MandrivaLinux-MoreApplications-Emulators;Emulator;
EOF

%files
%defattr(-,root,root)
%doc ../README.FIRST ../gpl-spanish.htm ../*.txt ../*.linux ../docs/* ../extras/*
%attr(0755,root,games) %{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}
%{_iconsdir}/*
%{_datadir}/applications/mandriva-%{name}.desktop

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}

%postun
%{clean_menus}
%endif

