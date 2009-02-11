Summary:	A gothic fantasy roguelike game
Summary(pl.UTF-8):	Gotycka gra fantasy typu rogue
Name:		wrogue
Version:	0.8.0b
Release:	1
License:	GPL v3+
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/todoom/%{name}-%{version}.zip
# Source0-md5:	977ccda1ac18ca3ee545fab95db56b2e
Source1:	%{name}.desktop
Source2:	%{name}.xpm
URL:		http://todoom.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2.9
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Warp Rogue is a gothic fantasy roguelike game. It features RPG-like
game mechanics, recruitable NPCs, and a consistent theme.

%description -l pl.UTF-8
Warp Rogue jest gotycką grą typu rogue. Gra zapewnia mechanikę
właściwą dla gier RPG oraz konsekwentny motyw.

%prep
%setup -q
%{__sed} -i 's@data/@%{_datadir}/%{name}/data/@' `grep -r -l 'data/' .`

# prevent from adding useless paths' prefixes
%{__sed} -ie '561d' src/lib/appdir.c

%build
cd src/
%{__make} -f linux.mak \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -I./include -I./lib `sdl-config --cflags`" \
	LDFLAGS="%{rpmldflags} `sdl-config --libs`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_desktopdir},%{_bindir},%{_pixmapsdir}}

cp -r data/ $RPM_BUILD_ROOT%{_datadir}/%{name}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changes.txt
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.xpm
