Summary:	A gothic fantasy roguelike game
Summary(pl.UTF-8):	Gotycka gra fantasy typu rogue
Name:		wrogue
Version:	0.8.0
Release:	1
License:	GPL v3+
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/todoom/%{name}-%{version}.tar.bz2
# Source0-md5:	c03ac3b590ec668a84965007d08126a9
Source1:	%{name}.desktop
Source2:	%{name}.xpm
Patch0:		%{name}-makefile.patch
URL:		http://todoom.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2.9
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Warp Rogue is a gothic fantasy roguelike game. It features RPG-like
game mechanics, recruitable NPCs, and a consistent theme.

%description -l pl.UTF-8
Warp Rogue jest gotycką grą typu rogue. Gra zapewnia mechanikę
właściwą dla gier RPG oraz konsekwentny motyw.

%prep
%setup -q
%patch0 -p1
%{__sed} -i 's@./data@%{_datadir}/%{name}/data@' src/platform/unix/platform_unix.c

%build
cd src/
%{__make} -f unix.mak \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -I. -I./lib `sdl-config --cflags`" \
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
%doc changes.txt scenario_guide.txt
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.xpm
